import sys
input = sys.stdin.readline
n,m = map(int,input().split())
a = list(map(int,input().split()))
start = 0
end = max(a)+1
while start < end:
    mid = (start + end) // 2+1
    s = sum([max(0,x-mid) for x in a])
    if s >= m:
        start = mid
    else:
        end = mid-1
print(start)

