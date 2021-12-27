def initials_only(first, middle, last):
    initials = first[0]+middle[0]+last[0]
                 
    return initials 

firstn = input("put your first name: ")
middlen = input("put your middle name: ")
lastn = input("put your last name: ")


initials=initials_only(firstn,middlen,lastn)

print("This is your initials,",initials)

