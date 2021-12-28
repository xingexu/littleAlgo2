ending = "XXX" 
word = ""
acronym = ""
while word != ending:
  word = input("Enter a word or \"XXX\" to finish")
  if word != ending:
     acronym = acronym + word[0] 
  
print(acronym)


acronym = ""
words = input("Enter words to be turned into an acronym: ")


words_list = words.split()

for word in words_list:
    acronym = acronym + word[0]
print(acronym)



