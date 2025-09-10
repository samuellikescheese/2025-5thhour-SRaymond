#Name:
#Class: 5th Hour
#Assignment: HW6


#1. Import the "random" library
import random
#2. print "Hello World!"
print("hello world")
#3. Create three different variables that each randomly generate an integer between 1 and 10
a = random.randint(1,10)
b = random.randint(1,10)
c = random.randint(1,10)
#4. Print the three variables from #3 on the same line.
print(a,b,c)
#5. Add 2 to the first variable in #3, Subtract 4 from the second variable in #3, and multiply by 1.5 the third variable in #3.
a += 2
b -= 4
c *= 1.5
#6. Print each result from #5 on the same line.
print(a,b,c)
#7. Create a list containing four variables that each randomly generate an integer between 1 and 6
list = [random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6)]
#8. Sort the list in #7 and print it.
list.sort()
print(list)
#9. Add together the highest three numbers in the list from #7 and print the result.
print(list[1] + list[2] + list[3])
#10. Create a list with 5 names of other students in this class and print the list.
sam = ["aiden", "hoegen", "ivan","brenlin","tristen"]
#11. Shuffle the list in #10 and print the list again.
random.shuffle(sam)
#12. Print a random choice from the list of names from #10.
print(sam[0])