x = 0
print ("hello world")
while 5 > 3:
    players = int(input("input how many players you have (more then 0)  "))
    if players < 1:
        print ("more then 0 stupid")
        continue
    count = players
    for i in range(0, players):
        score = int(input("input your score (1-5)"))
        if score > 5 or score < 1 :
            print ("1 tho 5 stupid")
            continue
        x += score
        print (score)
    y = x / count
    print (y)