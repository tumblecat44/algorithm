n = int(input())
a = list(map(int, input().split()))
s = []
res = [-1 for i in range(n)]
for i in range(len(a)):
    while s and a[s[-1]] < a[i]:
        res[s.pop()] = a[i]
    s.append(i)
print(*res)