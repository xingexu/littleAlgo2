obvious = ["password", "qwerty", "hello123", "letmein", "12345"]

password = input("Please enter a password: ")
for count in range(len(obvious)):
    if password == obvious[count]:
        print("This password is weak.")

if len(password) < 8:
    print("too short make it at least 8 characters")
    
char = 0
num = 0
upper = 0
lower = 0

for count in range(len(password)):
    if password[count].isdigit():
        num = num+1
    elif password[count].isalpha():
        char = char+1
        if password[count].isupper():
            upper = upper+1
        elif password[count].islower():
            lower = lower+1

if num == 0:
    print("inclue digits")
if upper == 0 or lower ==0:
    print(upper,lower,"include lower and uppercase letters")
if char == 0:
    print("include letters")
if num  > 0 and char > 0 and upper > 0 and lower > 0:
    print("Your password is good to go")