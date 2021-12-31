def generate_username (firstname, lastname):
    username = lastname + firstname[0]

    users_file = open("users.txt","r")
    usernames = eval(users_file.read())
    users_file.close()

    for count in range(len(usernames)):
        if usernames[count][0] == username:
            username = username + "#" 
    return username
forename = input("Enter your first name: ")
surname = input("Enter your surname: ")
username_out = generate_username(forename, surname)