cs_scores = [["Theo","45","60","72"],
            ["Angharad","55","65","70"],
            ["Sameer","71","78","78"],
            ["Adrian","68","79","80"],
            ["Ayana","98","85","91"]]

total = 0
for exam in range(1,4):
    for student in range(len(cs_scores)):
        total = total + int(cs_scores[student][exam])

mean = total/len(cs_scores)
print("Mean average for exam", exam, "is", mean)
total = 0
