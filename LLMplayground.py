#Name: samuel
#Class: 5th Hour
#Assignment: LLMplayground

def start():
    print("You wake up in a dark forest. There's a path to the left and right.")
    choice = input("Do you go left or right? (left/right): ").strip().lower()

    if choice == "left":
        left_path()
    elif choice == "right":
        right_path()
    else:
        print("Invalid choice. Try again.")
        start()

def left_path():
    print("You encounter a wild wolf!")
    choice = input("Do you run or fight? (run/fight): ").strip().lower()

    if choice == "run":
        print("You run away safely. You find a cabin and survive. You win!")
    elif choice == "fight":
        print("The wolf is too strong. You lose.")
    else:
        print("Invalid choice. Try again.")
        left_path()

def right_path():
    print("You find a treasure chest!")
    choice = input("Do you open it or leave it? (open/leave): ").strip().lower()

    if choice == "open":
        print("The chest is filled with gold! You win!")
    elif choice == "leave":
        print("You walk away, never knowing what was inside. The end.")
    else:
        print("Invalid choice. Try again.")
        right_path()

if __name__ == "__main__":
    start()