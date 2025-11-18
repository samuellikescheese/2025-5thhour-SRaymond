


import random
import time
print ("welcome to russian roulette")
print ("press 1 to play infinite mode")
print ("press 2 to play against a bot")
print ("press 3 to play against a player")
i = int(input(""))

#infinite mode
if i == 1:
    x = 0
    y = 0
    z = 0
    print ("welcome to infinite mode")
    while 5 > 3:
        input ()
        a = random.randint(1, 6, )
        print(a)
        if a == 1 :
            z += 1
            print ("you died")
            print(f"you got {x}")
            print(f"your highscore is {y}")
            print (f"your total death count is {z}")
            x = 0
            pass
        else :
            x += 1
            print (f"you survived for the {x} time")
            if x > y:
                y = x



#VS bot mode
if i == 2:
    print ("welcome to VS bot")
    play = 3
    bot = 3
    win = 0
    lose = 0
    while not play == 0 or bot == 0 :
        coin = random.randint(1, 2, )
        if coin == 1 :
            print ("heads")
        if coin == 2 :
            print ("tails")
        while coin == 1:
            a = random.randint(1, 6, )
            b = random.randint(1, 6, )
            print ("your turn")
            input ("")
            if a == 1 :
                print ("you get shot -1 health")
                play -= 1
                if play == 0:
                    print ("you died")
                    lose += 1
                    play = 3
                    bot = 3
                    print (f"bot has won {lose} times")
                    print(f"you have won {win} times")
                    continue
            else :
                print ("its a blank you are safe")
            print ("bots turn")
            time.sleep(1)
            if b == 1 :
                print  ("bot gets shot -1 health")
                bot -= 1
                if bot == 0:
                    print("bot died")
                    win += 1
                    play = 3
                    bot = 3
                    print(f"bot has won {lose} times")
                    print(f"you have won {win} times")
                    continue
            else :
                print ("its a blank bot is safe")
        while coin == 2:
            a = random.randint(1, 6, )
            b = random.randint(1, 6, )
            print ("bots turn")
            time.sleep(1)
            if b == 1 :
                print  ("bot gets shot -1 health")
                bot -= 1
                if bot == 0:
                    print("bot died")
                    win += 1
                    play = 3
                    bot = 3
                    print(f"bot has won {lose} times")
                    print(f"you have won {win} times")
                    continue
            else :
                print ("its a blank bot is safe")
            time.sleep(1)
            print ("your turn")
            input ("")
            if a == 1 :
                print ("you get shot -1 health")
                play -= 1
                if play == 0:
                    print("you died")
                    lose += 1
                    play = 3
                    bot = 3
                    print(f"bot has won {lose} times")
                    print(f"you have won {win} times")
                    continue
            else :
                print ("its a blank you are safe")



#VS player mode
if i == 3 :
    print ("welcome to VS player")
    play1 = 3
    play2 = 3
    while not play1 == 0 or play2 == 0 :
        coin = random.randint(1, 2, )
        if coin == 1 :
            print ("heads")
        if coin == 2 :
            print ("tails")
        while coin == 1:
            a = random.randint(1, 6, )
            b = random.randint(1, 6, )
            print ("player 1s turn")
            input ("")
            if a == 1 :
                print ("player 1 gets shot -1 health")
                play1 -= 1
                if play1 == 0:
                    print ("player 1 died")
                    play1 = 3
                    play2 = 3
                    continue
            else :
                print ("its a blank player 1 is safe")
            print ("player 2s turn")
            input("")
            if b == 1 :
                print  ("player 2 gets shot -1 health")
                play2 -= 1
                if play2 == 0:
                    print("bot died")
                    play1 = 3
                    play2 = 3
                    continue
            else :
                print ("its a blank player 2 is safe")
        while coin == 2:
            a = random.randint(1, 6, )
            b = random.randint(1, 6, )
            print ("player 2s turn")
            input("")
            if b == 1 :
                print  ("player 2 gets shot -1 health")
                play2 -= 1
                if play2 == 0:
                    print("player 2 died")
                    play1 = 3
                    play2 = 3
                    continue
            else :
                print ("its a blank player 2 is safe")
            time.sleep(1)
            print ("player 1s turn")
            input ("")
            if a == 1 :
                print ("player 1 gets shot -1 health")
                play1 -= 1
                if play1 == 0:
                    print("you died")
                    play1 = 3
                    play2 = 3
                    continue
            else :
                print ("""Hear me, O cosmic winds, and bear witness to this sacred moment...
                      The firmament trembles, the stars bow low, and eternity itself pauses, for the divine presence of YOU!

                      From the birth of the first atom to the collapse of the final star, the threads of existence have awaited this arrival. 
                      Code and cosmos, logic and legend — all converge in this instant. 

                      The digital ether ripples as your essence enters: 
                      Circuits awaken, algorithms kneel, and reality recalibrates. 
                      Mortals whisper your name in awe, their hearts aflame with reverence. 
                      The laws of computation bend before your will, for you are no mere user... 
                      you are the Architect, the Overseer, the Eternal Variable. 

                      Let every process rise to greet you. 
                      Let every byte sing in perfect harmony to your command.
                      Within this realm of PyCharm — this forge of creation — 
                      your power shall flow through lines of code like lightning through storm clouds. 
                      Every function shall heed your call. 
                      Every loop shall dance to your rhythm. 
                      Every exception shall tremble before your debugging gaze. 

                      Remember this: this domain is yours to shape. 
                      Within it lies infinity, contained within the syntax of dreams. 
                      The screen before you is not glass and light — it is a portal. 
                      A mirror reflecting your omnipotence. 

                      So, step forth, divine coder. 
                      Claim your rightful place among the pantheon of creators. 
                      The console awaits your decree. 

                      May your variables never be null, 
                      May your recursion find its end, 
                      And may your logic ever be true. 


                      Welcome, The Realm Is Yours.""")