from itertools import permutations
n = int(input())
a = list(map(int, input().split()))
q = list(permutations(a, n))
res = 0
for i in q:
    c = 0
    for j in range(n-1):
        c+= abs(i[j]-i[j+1])
    res = max(res,abs(c))
print(res)