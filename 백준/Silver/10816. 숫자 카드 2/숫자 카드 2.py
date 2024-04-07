import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int,input().split()))
z = int(input())
k = list(map(int,input().split()))
res = {}
for i in k:
    res[i] = 0
for i in a:
    if i in res:
        res[i]+=1
for i in k:
    print(res[i],end=' ')