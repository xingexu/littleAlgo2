cs_scores=[["Karman","45","60","72"],
          ["Daniel","55","65","70"],
          ["Parker","71","78","78"],
          ["Jessica","68","79","80"],
          ["Edie","98","85","91"]]

total = 0

for exam in range(1,4):
    for student in range(len(cs_scores)):
        total = total + int(cs_scores[student][exam])
    
    print("Total for exam num", exam, "equals", total)
    total = 0
    
