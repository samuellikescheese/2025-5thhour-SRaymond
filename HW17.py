#Name:samuel
#Class: 5th Hour
#Assignment: HW17
import random
#1. Create a def function that plays a single round of rock, paper, scissors where the user inputs
#1 for rock, 2 for paper, or 3 for scissors and compares it to a random number generated to serve
#as the "opponent's hand".
print ("welcome to rock, paper, scissors VS bot")
def game():
    print (" 1(rock)  2(paper) 3(scissors)")
    a = int(input())
    if not a == 1 and not a == 2 and not a == 3:
        print("try again")
        game()
    b = random.randint(1,3)
    if a == 1:
        print ("you picked rock")
    if a == 2:
        print ("you picked paper")
    if a == 3:
        print ("you picked scissors")
    if b == 1:
        print ("bot picked rock")
    if b == 2:
        print ("bot picked paper")
    if b == 3:
        print ("bot picked scissors")
    if a == 1 and b == 3 or a == 2 and b == 1 or a == 3 and b == 2:
        print ("you win")
    elif a == 3 and b == 1 or a == 1 and b == 2 or a == 2 and b == 3:
        print ("you lose")
    else:
        print ("you tie")
#2. Create a def function that prompts the user to input if they want to play another round, and
#repeats the RPS def function if they do or exits the code if they don't.
    print("do you want to play again? 1(yes)")
    c = int(input())
    if c == 1:
        game()
    else:
        print ("thank you for playing")
game()