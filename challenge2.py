def subtract(num1, num2):
    if num1 > num2:
        out = num1 - num2 
    else:
        out = num2 - num1
    return out

num1_enter = int(input("Enter a number: "))
num2_enter = int(input("Enter a number: "))

difference = subtract(num1_enter, num2_enter)

print("The difference is", difference)
 
