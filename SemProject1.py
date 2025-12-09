#Name:samuel raymond
#Class: 5th Hour
#Assignment: Semester Project 1

import random

#Due to weird time travelling circumstances beyond explanation, you find yourself in 2018 or so
#working for Larian Studios. Currently, they are working on the early prototypes of the hype
#upcoming game "Baldur's Gate 3". BG3 is a game that uses the Dungeons & Dragons 5th edition rules
#as its framework for gameplay. You have been given a basic dictionary of some of the main hero
#characters and some of the enemies they may face, and are tasked with making an early prototype
#of one of the party members fighting against an enemy until one of them hits zero HP (dies).

partyDict = {
    "LaeZel" : {
        "HO" : 48,
        "Init" : 1,
        "AC" : 17,
        "AtkMod": 6,
        "Damage" : random.randint(1,6) + random.randint(1,6) + 3
    },
    "Shadowheart" : {
        "HP" : 40,
        "Init" : 1,
        "AC" : 18,
        "AtkMod": 4,
        "Damage" : random.randint(1,6) + 3,
    },
    "Gale" : {
        "HP" : 32,
        "Init" : 1,
        "AC" : 14,
        "AtkMod": 6,
        "Damage" : random.randint(1,10) + random.randint(1,10),
    },
    "Astarion" : {
        "HP" : 40,
        "Init" : 3,
        "AC" : 14,
        "AtkMod": 5,
        "Damage" : random.randint(1,8) + random.randint(1,6) + 4,
    }
}

enemyDict = {
    "Goblin" : {
        "HP" : 7,
        "Init" : 0,
        "AC" : 12,
        "AtkMod": 4,
        "Damage" : random.randint(1,6) + 2
    },
    "Orc": {
        "HP" : 15,
        "Init": 1,
        "AC" : 13,
        "AtkMod": 5,
        "Damage" : random.randint(1,12) + 3
    },
    "Troll": {
        "HP" : 84,
        "Init": 1,
        "AC" : 15,
        "AtkMod": 7,
        "Damage" : random.randint(1,6) + random.randint(1,6) + 4
    },
    "Mindflayer": {
        "HP" : 71,
        "Init": 1,
        "AC" : 15,
        "AtkMod": 7,
        "Damage" : random.randint(1,10) + random.randint(1,10) + 4
    },
    "Dragon": {
        "HP" : 127,
        "Init": 2,
        "AC" : 18,
        "AtkMod": 7,
        "Damage" : random.randint(1,10) + random.randint(1,10) + random.randint(1,8) + 4
    },
}

#Combat consists of these steps:

#1. Rolling for 'initiative' to see who goes first. This is determined by rolling a
#20-sided die (d20) and adding their initiative modifier (If the roll is the same,
#assume the hero goes first).

#2. Rolling to attack. This is determined by rolling a 20-sided die (d20) and adding their
#attack modifier. The attack hits if it matches or is higher than the target's Armor Class (AC).
#If the d20 rolled to attack is an unmodified ("natural") 20, the attack automatically hits and
#the character deals double damage. If the d20 rolled to attack is an unmodified ("natural") 1,
#the attack automatically misses

#3. If the attack hits, roll damage and subtract it from the target's hit points.

#4. The second in initiative rolls to attack (and rolls damage) afterward.

#5. Repeat steps 2-5 until one of the characters is dead.
rollhero = random.randint(1,20) + partyDict["Gale"]["Init"]
rollevil = random.randint(1,20) + enemyDict["Mindflayer"]["Init"]
print ("you play as gale the hero")
print ("your enemy is the Mindflayer (kill it)")
if rollhero > rollevil or rollhero == rollevil:
    while 5 > 3:
        print ("Gale attacks the Mindflayer")
        hero = random.randint(1,20)
        evil = random.randint(1,20)
        if  not hero == 1 or hero + partyDict["Gale"]["AtkMod"] >= (enemyDict["Mindflayer"]["AC"]) or hero == 20:
            enemyDict["Mindflayer"]["HP"] -= partyDict["Gale"]["Damage"]
            if enemyDict["Mindflayer"]["HP"] <= 0:
                print ("the Mindflayer is dead")
                exit()
            else:
                print ("the Mindflayer stands")
        else :
            print ("he misses")
        print ("the Mindflayer attacks")
        if not evil == 1 or evil + enemyDict["Mindflayer"]["AtkMod"] >= (partyDict["Gale"]["AC"]) or evil == 20:
            partyDict["Gale"]["HP"] -= enemyDict["Mindflayer"]["AtkMod"]
            if partyDict["Gale"]["HP"] <= 0:
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
        if not evil == 1 or evil + enemyDict["Mindflayer"]["AtkMod"] >= (partyDict["Gale"]["AC"]) or evil == 20:
            partyDict["Gale"]["HP"] -= enemyDict["Mindflayer"]["AtkMod"]
            if partyDict["Gale"]["HP"] <= 0:
                print ("Gale is dead")
                exit()
            else:
                print ("Gale stands")
        else :
            print ("he misses")
        print("gale attacks the Mindflayer")
        if not hero == 1 or hero + partyDict["Gale"]["AtkMod"] >= (enemyDict["Mindflayer"]["AC"]) or hero == 20:
            enemyDict["Mindflayer"]["HP"] -= partyDict["Gale"]["Damage"]
            if enemyDict["Mindflayer"]["HP"] <= 0:
                print("the Mindflayer is dead")
                exit()
            else:
                print("the Mindflayer stands")
        else:
            print("he misses")