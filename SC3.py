#Name:samuel raymond
#Class: 5th Hour
#Assignment: SC3

#You have been transferred to a new team working on a mobile game that allows you to dress up a
#model and rate other models in a "Project Runway" style competition.

#They want to start prototyping the rating system and are asking you to make it.
#This prototype needs to allow the user to input the number of players, let each player rate
#a single model from 1 to 5, and then give the average score of all of the ratings.
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