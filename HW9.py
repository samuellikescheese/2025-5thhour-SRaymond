#Name: samuel raymond
#Class: 6th Hour
#Assignment: HW9
import random

#1. Print "Hello World!"
print("hello world")
#2. Create a list with three variables that each randomly generate a number between 1 and 100
to13 = [random.randint(1,100), random.randint(1,100) ,random.randint(1,100), ]
#3. Print the list.
print(to13)
#4. Create an if statement that determines which of the three numbers is the highest and prints the result.
if to13[0] > to13[1] and to13[0] > to13[2]:
    print("one is the biggest")
    num = to13[0]
elif to13[1] > to13[0] and to13[1] > to13[2]:
    print("two is the biggest")
    num = to13[1]
elif to13[2] > to13[0] and to13[2] > to13[1]:
    print("three is the biggest")
    num = to13[2]
elif to13[0] > to13[2] and to13[1] > to13[2]:
    print("one and two are the biggest")
    num = to13[0]
elif to13[2] > to13[0] and to13[1] > to13[0]:
    print("three and two are the biggest")
    num = to13[2]
elif to13[0] > to13[1] and to13[2] > to13[1]:
    print("one and three are the biggest")
    num = to13[1]
else:
    print("all are the biggest")
    num = to13[0]
#5. Tie the result (the largest number) from #4 to a variable called "num".

#6. Create a nested if statement that prints if num is divisible by 2, divisible by 3, both, or neither.
if num % 2 == 0:
    if num % 3 == 0:
        print ("it is divisible by 2 and 3")
    else:
        print ("it is divisible by 2")
elif num % 3 == 0:
    print ("it is divisible by 3")
else:
    print("it is not divisible by 3 or 2")