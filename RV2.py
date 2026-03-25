#Name:samuel
#Class: 5th Hour
#Assignment: HW-R2


#1. Print "Hello World!"
print ("Hello World!")
#2. Create an empty list.
lister = []
#3. Create a list that contains the names of everyone in the classroom.
listerc = ["sam","aiden","dylan","ivan","hogan","brenlyn","coach mack","ashton","bryson"]
#4. Print the list from #3, sort the list, then print the list again.
print (listerc)
listerc.sort()
print (listerc)
#5. Append 5 different integers into the empty list from #2 and print the list.
lister.append(5)
lister.append(2)
lister.append(4)
lister.append(3)
lister.append(1)
print (lister)
#6. Add together the middle three numbers in the list from #2 and print the result.
print (lister[1] + lister[2] + lister[3])
#7. Remove the very first number in the list from #2. Print the new first number.
lister.pop(0)
print (lister[0])
print (lister)
#8. Create a dictionary with three keys with respective values: your name, your grade, and your favorite color.
samdict = {
    "name" : "sam",
    "age" : 16,
    "color" : "mint"
}
#9. Using the update function, add a fourth key and value determining your favorite candy.
samdict.update({"candy" : "black licorice"})
#10. Print ONLY the values of the dictionary from #8.
print (samdict.values())