numbers = [9, 8, 72, 22, 21, 81, 2, 1, 11, 76, 32, 54]

def highest_num(numbers_in):
    highest = numbers_in[0]

    for count in range(len(numbers_in)):
        if highest < numbers_in[count]:
            highest = numbers_in[count]
    
    return highest

highest_out = highest_num(numbers)
print("The highest number is", highest_out)
    