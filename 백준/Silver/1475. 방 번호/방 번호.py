q = list(map(int,input()))
c = [0]*10
for i in q:
    if i == 9 or i == 6:
        c[9] +=1
    else:

        c[i] += 1
c[9] = round(c[9]/2+0.05)
print(max(c))