#Name:samuel
#Class: 5th Hour
#Assignment: HW15

#1. import the "random" library
import random
#2. print "Hello World!"
print ("hello world")
#3. Create three variables named a, b, and c, and allow the user to input an integer for each.
a = int(input("Enter a number"))
b = int(input("Enter a number"))
c = int(input("Enter a number"))
#4. Add a and b together, then divide the sum by c. Print the result.
print ((a + b) / 2)
#5. Round the result from #3 up or down, and then determine if it is even or odd.
d = (round((a + b) / 2))
print(d)
if d % 2 == 0 :
    print ("its even")
else:
    print ("its odd")
#6. Create a list of five different random integers between 1 and 10.
numlist = [random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10)]
#7. Print the 4th number in the list.
print (numlist[3])
#8. Append another integer to the end of the list, also random from 1 to 10.
numlist.append(random.randint(1,10))
#9. Sort the list from lowest to highest and then print the 4th number in the list again.
numlist.sort()
print (numlist[3])
#10. Create a while loop that starts at 1, prints i and then adds i to itself until it is greater than 100.
e = 0
while not e == 100:
    e += 1
    print (f"{e}i")
#11. Create a list containing the names of five other students in the classroom.
namelist = ["aiden", "ivan", "dylan", "hoegen", "brenlin"]
#12. Create a for loop that individually prints out the names of each student in the list.
for i in namelist:
    print (i)
#13. Create a for loop that counts from 1 to 100, but ends early if the number is a multiple of 10.
for i in range(1,101):
    print (i)
    if i % 10 == 0:
        break
#14. Free space. Do something creative. :)
print ("do you like cheese(yes or no)?")
cheese = input()
if cheese == "yes":
    print ("thank you :)")
else:
    print ("why would you say that :(")