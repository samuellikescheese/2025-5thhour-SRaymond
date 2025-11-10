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
        print (x)
