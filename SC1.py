#Name: samuel
#Class: 5th Hour
#Assignment: Scenario 1

#Scenario 1:
#You are a programmer for a fledgling game developer. Your team lead has asked you
#to create a nested dictionary containing five enemy creatures (and their properties)
#for combat testing. Additionally, the testers are asking for a way to input changes
#to the enemy's damage values for balancing, as well as having it print those changes
#to confirm they went through.

#It is up to you to decide what properties are important and the theme of the game.

dragons = {
    "white" : {
        "element" : "ice",
        "defence" : 10,
        "offence" : 15,
        "speed" : 10
    },
    "black": {
        "element": "acid",
        "defence": 15,
        "offence": 20,
        "speed":15
    },
    "green": {
        "element": "poison",
        "defence": 20,
        "offence": 25,
        "speed": 20
    },
    "blue": {
        "element": "lighting",
        "defence": 25,
        "offence": 30,
        "speed": 25
    },
    "red": {
        "element": "fire",
        "defence": 30,
        "offence": 35,
        "speed": 30
    }
}
print(dragons["red"]["offence"],dragons["blue"]["offence"],dragons["green"]["offence"],dragons["black"]["offence"],dragons["white"]["offence"])
dragons["white"]["offence"] = int(input())
dragons["black"]["offence"] = int(input())
dragons["green"]["offence"] = int(input())
dragons["blue"]["offence"] = int(input())
dragons["red"]["offence"] = int(input())
print(dragons["red"]["offence"],dragons["blue"]["offence"],dragons["green"]["offence"],dragons["black"]["offence"],dragons["white"]["offence"])
