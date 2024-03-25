T = int(input())
for _ in range(T):
    z = input()
    up = 0
    res = 0
    for i in range(len(z)):
        if z[i] == "O":
            up+=1
        else:
            up=0
        res+=up
    print(res)