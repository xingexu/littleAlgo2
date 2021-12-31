def vowel_counter(sentence):
    A = 0
    E = 0
    I = 0
    O = 0
    U = 0
    for count in range(len(sentence)):
        if sentence[count].upper() == "A":
            A = A+1
        elif sentence[count].upper() == "E":
            E = E+1
        elif sentence[count].upper() == "I":
            I = I+1
        elif sentence[count].upper() == "O":
            O =O+1
        elif sentence [count].upper() == "U":
            U = U+1
    
    print("total a's:", A)
    print("total e's:", E)
    print("total i's:", I)
    print("total o's:", O)
    print("total u's:", U)
    
    
sentence = "Xinge"
    
vowel_counter(sentence)
    
        