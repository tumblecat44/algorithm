import sys
input = sys.stdin.readline
t = int(input())
sik = list(map(int,input().split()))
sik.sort()
j = 0
res =0
for i in sik:
    j+=i
    res+=j
print(res)