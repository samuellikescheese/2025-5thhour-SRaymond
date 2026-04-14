#Name:samuel
#Class: 5th Hour
#Assignment: HW_R7


#1. Create a class containing a def function that inits self and the three attributes: name, grade, color.
class mesa:
    def __init__(self, name, grade, color):
        self.name = name
        self.grade = grade
        self.color = color
    def cheese(self):
        if self.grade >= 12:
            self.grade = "graduated"
        else:
            self.grade += 1
    def colored(self):
        a = int(input("do you want to change your favrite color 1(yes) 2(no)"))
        if a == 1:
            self.color = input("your favrite color here")
        if a == 2:
            print ("it stays the same then")
#2. Make a def function within the class that adds 1 to the grade attribute to any object called to it.
#If they are 12th grade, have the code change their grade to "graduated" instead.

#3. Make a def function within the class that offers the user to input/change their favorite color.