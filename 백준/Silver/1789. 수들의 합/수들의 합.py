s = int(input())
res = 0
z = 0
if s == 1:
    print(1)
else:
    for i in range(1,s+1):
        res+=i
        if res > s:
            print(i-1)
            break