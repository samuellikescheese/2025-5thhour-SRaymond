#Name:samuel
#Class: 5th Hour
#Assignment: HW-R6


#1. Create a def function that prints out "Hello World!". Call the function.
def Hello():
    print ("Hello world!")
Hello()
#2. Create a def function that prints your name. Call the function with the name as the argument.
def name(cool):
    print(cool)
name("sam")
#3. Create a def function that calculates the average of a list. Call the function with the list as the argument.
def lister(*numb):
    silso = sum(numb)
    print (silso / len(numb))
lister(1,5,10,7,9)
#4. Call the function from #3 but with a new list of different numbers.
lister(6,8,4,200,1)
#5. Create a def function that takes two numbers as arguments, x and y. Inside the function, create a for loop
#with a range of 10. Inside the loop, make z equal the sum of x and y, make x equal y, then y equal z.
def stupid(x,y):
    for i in range(10):
        z = x + y
        x = y
        y = z
        print (x)
#6. Call the function from #5 with the arguments for x and y being 0 and 1.
stupid(0,1)