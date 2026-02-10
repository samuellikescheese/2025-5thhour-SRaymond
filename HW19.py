#Name:samuel
#Class: 5th Hour
#Assignment: HW19

#1. Import the def functions created in problem 1-4 from HW16
from HW16 import *
#2. Call the functions here and run HW19
me()
avg(4,6,2)
ani("monkey", "ant", "elephant", "pony", "gorilla")
num(6)
#3. Delete all calls from HW16 and run HW19 again.
#4. Create a try catch that tries to print variable x (which has no value), but prints "Hello World!" instead.
try:
    print(sam)
except:
    print("Hello World!")
#5. Create a try catch that tries to divide 100 by whatever number the user inputs, but prints an exception for Divide By Zero errors.
try:
    bee = int(input())
    print (100 / bee)
except:
    print ("error diveded by zero")
#6. Create a variable that asks the user for a number. If the user input is not an integer, prints an exception for Value errors.
try:
    u = int(input("Give me an integer"))
    print(u)
except:
    print ("It needs to be an integer!")
#7. Create a while loop that counts down from 5 to 0, but raises an exception when it counts below zero.
count = 5
while True:
    try:
        print(count)
        count -= 1
        if count < 0:
            raise ValueError("Value went below zero!")
    except ValueError as e:
        print(e)
        break
# my monster
