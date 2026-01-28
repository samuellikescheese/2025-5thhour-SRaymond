#Name:samuel
#Class: 5th Hour
#Assignment: HW18


#1. Import the "random" library and create a def function that prints "Hello World!"
import random
from traceback import print_tb


def hello():
    print ("hello world")
#2. Create two empty integer variables named "heads" and "tails"
heads = 0
tails = 0
#3. Create a def function that flips a coin one hundred times and increments the result in the above variables.
def countdown():
    global heads, tails
    for i in range(0,100):
        a = random.randint(1,2)
        if a == 1:
            heads +=1
        else:
            tails +=1
#4. Call the "Hello world" and "Coin Flip" functions here
hello()
countdown()
#5. Print the final result of heads and tails here
print(heads)
print(tails)
#6. Create a list called beanBag and add at least 5 different colored beans to the list as strings.
beanbag = ["University of Pennsylvania red","Purple Mountain Majesty","International Klein Blue","Pease-porridge tawny","Quercitron"]
#7. Create a def function that pulls a random bean out of the beanBag list, prints which bean you pulled, and then removes it from the list.
def bean():
    b = random.choice(beanbag)
    print (b)
    beanbag.remove(b)
#8. Create a def function that asks if you want to pull another bean out of the bag and, if yes, repeats the #3 def function
def iff():
    player = input("Y/N do you want to play again? ")
    if player == "Y" or player == "y" or player == "yes" or player == "Yes" or player == "1":
        print ("lets play again")
        bean()
    else :
        print ("Thank you for playing")
#9. Call the "Bean Pull" function here
bean()
iff()