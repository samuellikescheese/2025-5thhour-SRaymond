import random
random_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
card = random.choice(random_list)
print(card)
while 5 > 3:
    card = random.choice(random_list)
    int(input())
    x = card
    random_list.remove(card)
    if card == 13:
        print("king")
    elif card == 12:
        print("queen")
    elif card == 11:
        print("Jack")
    else :
        print(card)
    random_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
