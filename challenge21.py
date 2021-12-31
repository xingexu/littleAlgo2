num = [9, 98, 72, 1002, 21, 81, 2, 1, 101, 76, 32, 54]

highest_num = num[0]

for i in range(len(num)):
    if highest_num < num[i]:
        highest_num = num[i]

print("The highest number is", highest_num)
    
    