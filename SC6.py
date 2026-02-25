#Name:samuel
#Class: 5th Hour
#Assignment: Scenario 6

import random

#With a fresh perspective, the team lead wants you to look back and refactor the old combat code to
#be streamlined with classes so the character and enemy stats won't be built in bulky dictionaries anymore.

#(Translation: Rebuild Semester Project 1 using classes instead of dictionaries, include and refactor
#the combat test code below as well.)
class noob:
    def __init__ (self, HP, Init, AC, Atkmod, Damage):
        self.HP = HP
        self.Init = Init
        self.AC = AC
        self.Atkmod = Atkmod
        self.Damage = Damage
Laezel = noob(48, 1, 17, 6, random.randint(1,6) + random.randint(1,6) + 3)
Shadowheart = noob(40, 1, 18, 4, random.randint(1,6) + 3)
Gale = noob(40, 1, 14, 6, random.randint(1,10) + random.randint(1,10))
Astarion = noob(40, 3, 14, 5, random.randint(1,8) + random.randint(1,6) + 4)
Goblin = noob(7, 0, 12, 4, random.randint(1,6) + 2)
Orc = noob(15,1,13,5,random.randint(1,12) + 3)
Troll = noob(84,1,15,7,random.randint(1,6) + random.randint(1,6) + 4)
Mindflayer = noob(71,1,15,7,random.randint(1,10) + random.randint(1,10) + 4)
Dragon = noob(127, 2, 18,7,random.randint(1,10) + random.randint(1,10) + random.randint(1,8) + 4)




rollhero = random.randint(1,20) + Gale.Init
rollevil = random.randint(1,20) + Mindflayer.Init

print ("you play as gale the hero")
print ("your enemy is the Mindflayer (kill it)")
if rollhero > rollevil or rollhero == rollevil:
    while 5 > 3:
        print ("Gale attacks the Mindflayer")
        hero = random.randint(1,20)
        evil = random.randint(1,20)
        if  not hero == 1 or hero + Gale.Atkmod >= Mindflayer.AC or hero == 20:
            Mindflayer.HP -= Gale.Damage
            if Mindflayer.HP <= 0:
                print ("the Mindflayer is dead")
                exit()
            else:
                print ("the Mindflayer stands")
        else :
            print ("he misses")
        print ("the Mindflayer attacks")
        if not evil == 1 or evil + Mindflayer.Atkmod >= Gale.AC or evil == 20:
            Gale.HP -= Mindflayer.Atkmod
            if Gale.HP <= 0:
                print ("Gale is dead")
                exit()
            else:
                print ("Gale stands")
        else :
            print ("he misses")
if rollevil > rollhero:
    while 5 > 3:
        print ("the Mindflayer attacks")
        hero = random.randint(1, 20)
        evil = random.randint(1, 20)
        if not evil == 1 or evil + Mindflayer.Atkmod >= Gale.AC or evil == 20:
            Gale.HP -= Mindflayer.Atkmod
            if Gale.HP <= 0:
                print ("Gale is dead")
                exit()
            else:
                print ("Gale stands")
        else :
            print ("he misses")
        print("gale attacks the Mindflayer")
        if not hero == 1 or hero + Gale.Atkmod >= Mindflayer.AC or hero == 20:
            Mindflayer.HP -= Gale.Damage
            if Mindflayer.HP <= 0:
                print("the Mindflayer is dead")
                exit()
            else:
                print("the Mindflayer stands")
        else:
            print("he misses")