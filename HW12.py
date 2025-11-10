#Name:
#Class: 5th Hour
#Assignment: HW12
import random
#1. Create a while loop with variable i that counts down from 5 to 0 and then prints
#"Hello World!" at the end.
i = 5
while i > -1 :
    print (i)
    i -= 1
print ("hello world")
#2. Create a while loop that prints only even numbers between 1 and 30 (HINT: modulo).
num = 0
while num < 30 :
    num += 1
    if num % 2 == 0 :
        print (num)

#3. Create a while loop that continues (skips the number) if the number is divisible by 3.
mun = 0
while mun < 30 :
    mun += 1
    if mun % 3 == 0 :
        continue
    else:
        print (mun)
#4. Create a while loop that randomly generates a number between 1 and 6, prints the result,
#and then breaks the loop if it's a 1.
rand = random.randint(1,6)
print (rand)
while rand > 1 :
    rand = random.randint(1,6)
    print (rand)
    if rand == 1 :
        break
#5. Create a while loop that asks for a number input until the user inputs the number 0.
g = int(input())
while not g == 0 :
    print ("try again")
    g = int(input())