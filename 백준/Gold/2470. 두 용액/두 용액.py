import sys
import bisect

input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
a.sort() 

min_res = sys.maxsize
res = []

for i in range(n):
    left, right = i + 1, n - 1
    target = -a[i]

    idx = bisect.bisect_left(a, target, left, right + 1)

    for j in [idx - 1, idx]:
        if left <= j <= right and abs(a[i] + a[j]) < min_res:
            min_res = abs(a[i] + a[j])
            res = [a[i], a[j]]
print(*res)
