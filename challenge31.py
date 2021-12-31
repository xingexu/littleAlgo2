def vowel_counter(sentence):
    vowel_list=[ ["A",0],
                 ["E",0],
                 ["I",0],
                 ["O",0],
                 ["U",0]]

    #for each character
    for count in range(len(sentence)):
        #for each vowel in the vowel_list
        for letter in range(len(vowel_list)):
            #if the character == vowel
            if sentence[count].upper() == vowel_list[letter][0]:
                #increment that vowel's counter
                vowel_list[letter][1] = (vowel_list[letter][1])+1
             
    #  loop through each vowel in vowel_list and output their totals
    for vowels in range(len(vowel_list)):
        print("The number of",vowel_list[vowels][0],"is",vowel_list[vowels][1])
        
    
sentence = "Learning programming is similar to learning a musical instrument. Both involve practice and making lots of mistakes. Both also require perseverence to develop fluency. Keep going!"
    
vowel_counter(sentence)
    
        