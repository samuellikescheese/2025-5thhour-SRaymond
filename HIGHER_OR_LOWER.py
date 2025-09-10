import random
random_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(random_list)
card = random.choice(random_list)
if card == 13:
    print("king")
elif card == 12:
    print("queen")
elif card == 11:
    print("Jack")
else :
    print(card)
