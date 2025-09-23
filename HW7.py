#Name:samuel
#Class: 5th Hour
#Assignment: HW7

#1. Print Hello World!
print("hello world")
#2. Create a dictionary with 3 keys and a value for each key. One of the keys must have a value with a list containing
#three numbers inside.
sandwitch = {
    "bread" : "white",
    "meat" : "smoked ham",
    "cheese" : [1,3,5]
}
#3. Print the keys of the dictionary from #2.
print(sandwitch.keys())
#4. Print the values of the dictionary from #2
print(sandwitch.values())
#5. Print one of the three numbers from the list by itself
print(sandwitch['cheese'][1])
#6. Using the update function, add a fourth key to the dictionary and give it a value.
sandwitch.update({"plant" : "luttuse"})
#7. Print the entire dictionary from #2 with the updated key and value.
print(sandwitch)
#8. Make a nested dictionary with three entries containing the name of another classmate and two other pieces of information
#within each entry.
sam = {
    "student_1" : {
        "Name" : "aiden",
        "Grade" : 10,
        "Games" : True
    },
    "student_2" : {
        "Name" : "Ivan",
        "Grade" : 12,
        "Games" : True
    },
    "student_3" : {
        "Name" : "Dylan",
        "Grade" : 12,
        "Games" : True
    },
}
#9. Print the names of all three classmates on the same line.
print(sam['student_1']['Name'], sam['student_2']['Name'], sam['student_3']['Name'])
#10. Use the pop function to remove one of the nested dictionaries inside and print the full dictionary from #8.
sam.pop('student_1')
print(sam)