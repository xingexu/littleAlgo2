ending = "XXX"
word = ""
acronym = ""
while word != ending: 
  word = input("Enter a word or XXX to finish: ")
  if word != ending:
     acronym = acronym + word[0] 
  
print(acronym)
