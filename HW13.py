#Name:sam
#Class: 5th Hour
#Assignment: HW13
import time
#A common exercise in computer science is "FizzBuzz". The rules of
#the game are simple. Count from 1 to 100 but with every number that
#is divisible by 3 you say "Fizz" instead of the number,
#every number divisible by 5 you say "Buzz" instead,
#and if it's divisible by both you say "FizzBuzz".

#Create a while loop that follows the rules of the game.







x = 0
while x < 1000:
    time.sleep(0.5)
    x += 1





    if x % 3 == 0 and x % 5 == 0 and x % 7 == 0:
        print ("fizzbuzzsam")
    elif x % 3 == 0 and x % 5 == 0:
        print ("fizzbuzz")
    elif x % 5 == 0 and x % 7 == 0:
        print ("buzzsam")
    elif x % 3 == 0 and x % 7 == 0:
        print ("fizzsam")
    elif x % 3 == 0:
        print ("fizz")
    elif x % 5 == 0:
        print ("buzz")
    elif x % 7 == 0:
        print ("sam")
    else:
        print("""Hear me, O cosmic winds, and bear witness to this sacred moment...
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
