#Name:samuel
#Class: 5th Hour
#Assignment: HW4


#1. Print Hello World!
print("hello world")
#1. Create a list with 5 strings containing 5 different names in it.
lisst = ["red", "blue", "green", "yellow", "pink"]
#2. Append a new name onto the Name List.
lisst.append("black")
#3. Print out the 4th name on the list.
print(lisst[3])
#4. Create a list with 4 different integers in it.
num = [1,2,3,4]
#5. Insert a new integer into the 2nd spot and print the new list.
num.insert(1,5)
print (num)
#6. Sort the list from lowest to highest and print the sorted list.
num.sort()
print(num)
#7. Add the 1st three numbers on the sorted list together and print the sum.
print(num[0] + num[1] + num[2])
#8. Create a list with two strings, two variables, and too boolean values.
bool = ["True", "False", True, False, 1, 0]
#9. Create a print statement that asks the user to input their own index value for the list on #8.
print(bool[int(input())])