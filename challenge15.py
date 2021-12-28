def is_multiple(x_in, y_in):
  if x_in % y_in == 0: 
    print(x_in, "is  a multiple of", y_in)
  else:
    print(x_in, "is not a multiple of", y_in)
       
print("A program to check if x is a multiple of y")
x = int(input("Enter a number to check if it is a multiple: "))
y = int(input("Enter a number to divide by: "))
#Call the procedure, passing in x and y
is_multiple(x,y)
