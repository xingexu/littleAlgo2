import random

one = 1
two = 2

while one != two:
    one = random.randint(1,6)
    two = random.randint(1,6)
    
    print("Dice 1 rolled:" + str(one))
    print("Dice 2 rolled:" + str(two))
    
    if one == two:
        print("Game loading")
    else:
        again = input("Press enter to roll again: ")
        
import random
