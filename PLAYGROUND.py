
import random
new = int(input())
if new == 1:
    while 5 > 3:
        input()
        a = random.randint(1,6)
        b = random.randint(1,6)
        c = random.randint(1,6)
        d = random.randint(1,6)
        print(a, b, c, d)
        if a==b==c==d :
            print ("QUADRUPLE")
        elif a==b and c==d or a==c and b==d or a==d and b==c :
            print ("2 DOUBLES")
        elif a==b==c or b==c==d or c==d==a or d==a==b :
            print ("TRIPLE")
        elif a==b or a==c or b==c or a==d or b==d or c==d:
            print ("DOUBLE")
        else :
            print ("nothing")
if new == 2:
    a = random.randint(1, 6)
    b = random.randint(1, 6)
    c = random.randint(1, 6)
    d = random.randint(1, 6)
    x1 = 0
    x2 = 0
    x3 = 0
    x4 = 0
    x5 = 0
    x6 = 0
    if a == 1 :
        x1 += 1
    if b == 1 :
        x1 += 1
    if c == 1 :
        x1 += 1
    if d == 1 :
        x1 += 1
    if a == 2 :
        x2 += 1
    if b == 2 :
        x2 += 1
    if c == 2 :
        x2 += 1
    if d == 2 :
        x2 += 1
























