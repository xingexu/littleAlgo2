import random

keeper = ["left", "centre", "right"]

k_score = 0
p_score = 0
for count in range(5):
    position = random.choice(keeper)

    player = input("Where do you want to score: ")

    print("Keeper went to the", position)

    if keeper == player:
        print("Penalty saved")
        k_score = k_score+1
    else:
        print("You scored!")
        p_score = p_score+1

if k_score > p_score:
    print("Keeper wins", k_score, "-", p_score)
else:
    print("You win!", p_score, "-", k_score)
        
    