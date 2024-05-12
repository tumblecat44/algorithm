import sys
input = sys.stdin.readline
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
a.sort(key=lambda x: (x[1],x[0]))
res = 0
endtime = 0
for i in a:
    if i[0] >= endtime:
        res += 1
        endtime = i[1]
print(res)