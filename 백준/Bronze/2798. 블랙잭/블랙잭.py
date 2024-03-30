from itertools import combinations
N,M = map(int,input().split())
arr = list(map(int,input().split()))
z = list(combinations(arr,3))
res = 0
for i in z:
    if sum(i) <= M:
        if sum(i) > res:
            res = sum(i)
print(res)