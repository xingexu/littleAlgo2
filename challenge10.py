def subject_short(subject):
    short = subject[0:3]
                 
    return short 

sub = input("What is the subject name? ")

sub_out=subject_short(sub)

print(sub,"becomes",sub_out)
