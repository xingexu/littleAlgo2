def options(num):
     if num == 1:
         return "Computer Science"
     elif num == 2:
         return "Music"
     elif num == 3:
         return "Dance" 
     elif num == 4:
         return "PE" 
     else:  
         return "Error"

def main():
     print("""
1 Computer Science
2 Music
3 Dance
4 PE
     """)
     opt_num = int(input("Enter a number to choose an option: "))
     subject = options(opt_num)
     if subject == "Error":
          print("You entered an invalid number")
          print("Please enter a number between 1 and 4")
          return main()
     else:
          print("You chose", subject)
main()