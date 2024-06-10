fs = 0
frhq =  0
for i in range(20):
    major,gim,grade = input().split()
    credit = int(gim[0])
    if grade == "P":
        pass
    else:
        frhq += credit
    if grade == "A+":
        fs = fs+credit*4.5
    elif grade == "A0":
        fs = fs+credit*4
    elif grade == "B+":
        fs = fs+credit*3.5
    elif grade == "B0":
        fs = fs+credit*3
    elif grade == "C+":
        fs = fs+credit*2.5
    elif grade == "C0":
        fs = fs+credit*2
    elif grade == "D+":
        fs = fs+credit*1.5
    elif grade == "D0":
        fs = fs+credit*1
    elif grade == "F":
        pass
print(fs/frhq)
