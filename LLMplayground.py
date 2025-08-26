import random
import os
import sys
import time
import threading
import json
import winsound  # Only works on Windows for sound (we'll make it optional)

try:
    import keyboard
    USE_KEYBOARD_MODULE = True
except ImportError:
    USE_KEYBOARD_MODULE = False

# === Configuration ===
WIDTH, HEIGHT = 30, 20
SNAKE_HEAD = '◉'
SNAKE_BODY = '●'
FOOD_CHAR = '✸'
OBSTACLE_CHAR = '■'
EMPTY_CHAR = ' '
BORDER_CHAR = '█'

WRAP_AROUND = False  # Snake wraps around edges if True
ENABLE_COLOR = True  # Set to False if colors don't work well
ENABLE_SOUND = True  # Toggle sound effects (only works on Windows)

HIGH_SCORE_FILE = "snake_highscore.json"

# === Colors ===
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    CYAN = '\033[96m'
    RESET = '\033[0m'

def colorize(text, color):
    return f"{color}{text}{Colors.RESET}" if ENABLE_COLOR else text

# === Globals ===
direction = 'RIGHT'
snake = []
food = ()
obstacles = set()
score = 0
high_score = 0
game_over = False
paused = False
exit_game = False
power_up = None
power_up_timer = 0
score_multiplier = 1

direction_lock = threading.Lock()
pause_lock = threading.Lock()
state_lock = threading.Lock()

# === Utility functions ===
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def load_high_score():
    global high_score
    if os.path.exists(HIGH_SCORE_FILE):
        try:
            with open(HIGH_SCORE_FILE, 'r') as f:
                data = json.load(f)
                high_score = data.get("high_score", 0)
        except Exception:
            high_score = 0
    else:
        high_score = 0

def save_high_score():
    try:
        with open(HIGH_SCORE_FILE, 'w') as f:
            json.dump({"high_score": high_score}, f)
    except Exception:
        pass

def play_sound(frequency=500, duration=200):
    if ENABLE_SOUND:
        winsound.Beep(frequency, duration)

def place_food():
    while True:
        pos = (random.randint(1, HEIGHT-2), random.randint(1, WIDTH-2))
        if pos not in snake and pos not in obstacles:
            return pos

def place_obstacle():
    while True:
        pos = (random.randint(1, HEIGHT-2), random.randint(1, WIDTH-2))
        if pos not in snake and pos != food and pos not in obstacles:
            return pos

def place_power_up():
    while True:
        pos = (random.randint(1, HEIGHT-2), random.randint(1, WIDTH-2))
        if pos not in snake and pos != food and pos not in obstacles:
            return pos

def print_board():
    clear_screen()
    print(f"Score: {score}  High Score: {high_score}    Controls: W/A/S/D or Arrow Keys = Move | P = Pause | Q = Quit")
    print(BORDER_CHAR * WIDTH)
    for y in range(1, HEIGHT-1):
        row = BORDER_CHAR
        for x in range(1, WIDTH-1):
            pos = (y, x)
            if pos == snake[0]:
                row += colorize(SNAKE_HEAD, Colors.YELLOW)
            elif pos in snake[1:]:
                row += colorize(SNAKE_BODY, Colors.GREEN)
            elif pos == food:
                row += colorize(FOOD_CHAR, Colors.RED)
            elif pos in obstacles:
                row += colorize(OBSTACLE_CHAR, Colors.CYAN)
            elif pos == power_up:
                row += colorize("★", Colors.GREEN)
            else:
                row += EMPTY_CHAR
        row += BORDER_CHAR
        print(row)
    print(BORDER_CHAR * WIDTH)
    if paused:
        print(colorize("\n--- PAUSED --- Press P to resume ---", Colors.YELLOW))

def countdown(seconds=3):
    for i in range(seconds, 0, -1):
        print(colorize(f"\rResuming in {i}...", Colors.YELLOW), end='', flush=True)
        time.sleep(1)
    print("\r" + " " * 20 + "\r", end='')

# === Game Logic ===
def move_snake():
    global score, food, game_over, obstacles, power_up, power_up_timer, score_multiplier

    head_y, head_x = snake[0]

    with direction_lock:
        dir = direction

    if dir == 'UP':
        head_y -= 1
    elif dir == 'DOWN':
        head_y += 1
    elif dir == 'LEFT':
        head_x -= 1
    elif dir == 'RIGHT':
        head_x += 1

    if WRAP_AROUND:
        head_y = (head_y - 1) % (HEIGHT - 2) + 1
        head_x = (head_x - 1) % (WIDTH - 2) + 1
    else:
        if head_y == 0 or head_y == HEIGHT - 1 or head_x == 0 or head_x == WIDTH - 1:
            game_over = True
            return

    new_head = (head_y, head_x)

    if new_head in snake or new_head in obstacles:
        game_over = True
        return

    snake.insert(0, new_head)

    if new_head == food:
        score += score_multiplier
        play_sound(600, 100)  # Food sound
        food = place_food()
        if score % 3 == 0 and len(obstacles) < 10:
            obstacles.add(place_obstacle())
        if random.random() < 0.2:  # 20% chance to spawn power-up
            power_up = place_power_up()
        else:
            power_up = None
    elif new_head == power_up:
        score_multiplier = 2  # Double score for the next food
        power_up = None
        power_up_timer = time.time()
    else:
        snake.pop()

    # Power-up timer
    if power_up_timer and time.time() - power_up_timer > 10:
        score_multiplier = 1  # Reset multiplier after 10 seconds

def input_thread_func():
    global direction, game_over, paused, exit_game
    if USE_KEYBOARD_MODULE:
        while not game_over and not exit_game:
            if keyboard.is_pressed('q'):
                with state_lock:
                    game_over = True
                    exit_game = True
                break
            if keyboard.is_pressed('p'):
                with pause_lock:
                    paused = not paused
                    if not paused:
                        countdown(3)
                time.sleep(0.3)

            with direction_lock:
                if not paused:
                    if keyboard.is_pressed('w') or keyboard.is_pressed('up'):
                        if direction != 'DOWN':
                            direction = 'UP'
                    elif keyboard.is_pressed('s') or keyboard.is_pressed('down'):
                        if direction != 'UP':
                            direction = 'DOWN'
                    elif keyboard.is_pressed('a') or keyboard.is_pressed('left'):
                        if direction != 'RIGHT':
                            direction = 'LEFT'
                    elif keyboard.is_pressed('d') or keyboard.is_pressed('right'):
                        if direction != 'LEFT':
                            direction = 'RIGHT'
            time.sleep(0.02)
    else:
        # fallback input for systems without 'keyboard' module
        while not game_over and not exit_game:
            key = None
            if os.name == 'nt':
                import msvcrt
                if msvcrt.kbhit():
                    key = msvcrt.getch()
                    if key in [b'\xe0', b'\x00']:  # arrow keys prefix
                        arrow_key = msvcrt.getch()
                        key_map = {b'H': 'up', b'P': 'down', b'K': 'left', b'M': 'right'}
                        key = key_map.get(arrow_key, None)
                    else:
                        try:
                            key = key.decode('utf-8').lower()
                        except:
                            key = None
            else:
                import sys, termios, tty, select
                fd = sys.stdin.fileno()
                old_settings = termios.tcgetattr(fd)
                try:
                    tty.setcbreak(fd)
                    dr, _, _ = select.select([sys.stdin], [], [], 0.1)
                    if dr:
                        key = sys.stdin.read(1).lower()
                finally:
                    termios.tcset
