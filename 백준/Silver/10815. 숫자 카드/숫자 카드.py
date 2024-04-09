N = int(input())
a = set(map(int,input().split()))
M = int(input())
z = list(map(int,input().split()))
res = []
for i in z:
    if i in a:
        res.append(1)
    else:
        res.append(0)
print(*res)