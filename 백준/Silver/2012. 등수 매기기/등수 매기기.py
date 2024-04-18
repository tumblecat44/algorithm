import sys
input = sys.stdin.readline
n = int(input())
dap = [i for i in range(1,n+1)]
zz = []
res = 0
for i in range(n):
    zz.append(int(input()))
zz.sort()
for i in range(n):
    res+=abs(dap[i]-zz[i])
print(res)