import random
score = 0

for i in range(3):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    
    print("Dice 1 rolled:" + str(dice1))
    print("Dice 2 rolled:" + str(dice2))
    
    total = dice1 + dice2
    print("Your total for this round is: ",total)

    score = score + total
    print("Your running score is now:", score)
    
print("Your final score is:", score)
