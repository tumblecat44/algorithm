import sys
input = sys.stdin.readline
t = int(input())
a = [int(input()) for _ in range(t)]
res = []
a.sort()
for i in range(t-2):
    ss = []
    if a[i] + a[i+1] > a[i+2]:
        ss.append(a[i])
        ss.append(a[i+1])
        ss.append(a[i+2])
        res.append(sum(ss))

if res:
    print(max(res))
else:
    print(-1)