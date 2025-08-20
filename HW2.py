#Name: samuel
#Class: 5th Hour
#Assignment: HW2


#1. Print "Hello World!"
print("hello world")
#2. Create three different variables with distinct names and values: one with an integer, one with a string, one with a boolean.
sam = 5
aiden = "no"
gage = False
#3. Print all three variables on the same print function (at the same time).
print(sam, aiden, gage)
#4. Create a variable that asks the user to input an integer.
intup = int(input())
#5. Add the integer variable from #2 with the integer from #4 and print the result.
anser = sam + intup
print(anser)
#6. Take the result from #5 and divide it by 2. Print the result.
ban = anser / 2
print(ban)
#7. Change the value of the boolean variable to the opposite value (if true then make false, or vice versa).
if gage == True :
    gage = False
else:
    gage = True
#8. Print the value of the boolean variable.
print(gage)
#9. Create a variable with a number that contains decimals.
eat = 6.6
#10. Round the number from #9 up or down using the round function.
print(round(eat))