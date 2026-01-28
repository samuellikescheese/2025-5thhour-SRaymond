import random
red = int(input())
blue = int(input())
green = int(input())
shotgun = []
while red > 0:
    shotgun.append("red")
    red -= 1
while blue > 0:
    shotgun.append("blue")
    blue -= 1
while green > 0:
    shotgun.append("green")
    green -= 1
print (shotgun)
while 5 > 3 :
    input()
    random.shuffle(shotgun)
    print (shotgun[0])
    shotgun.remove(shotgun[0])
    if shotgun == []:
        red = int(input())
        blue = int(input())
        green = int(input())
        shotgun = []
        while red > 0:
            shotgun.append("red")
            red -= 1
        while blue > 0:
            shotgun.append("blue")
            blue -= 1
        while green > 0:
            shotgun.append("green")
            green -= 1
        print(shotgun)