#Name: samuel
#Class: 5th Hour
#Assignment: HW5

#1. Create a list with 9 different numbers inside.
num = [73,68,45,92,12,34,87,47,58]
#2. Sort the list from highest to lowest.
num.sort(reverse=True)
#3. Create an empty list.
dude = []
#4. Remove the median number from the first list and add it to the second list.
dude.append(num[4])
num.pop(4)
#5. Remove the first number from the first list and add it to the second list.
dude.append(num[0])
num.pop(0)
#6. Print both lists.
print(num)
print(dude)
#7. Add the two numbers in the second list together and print the result.
dude[0] = dude[0] + dude[1]
dude.pop(1)
print(dude[0])
#8. Move the number back to the first list (like you did in #4 and #5 but reversed).
num.append(dude[0])
dude.pop(0)
#9. Sort the first list from lowest to highest and print it.
num.sort()
print(num)