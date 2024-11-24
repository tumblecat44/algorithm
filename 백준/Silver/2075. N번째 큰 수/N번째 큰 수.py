import heapq, sys
input = sys.stdin.readline
n = int(input())
a = []
for i in range(n):
    for j in list(map(int, input().split())):
        heapq.heappush(a,j)
        if len(a) > n:
            heapq.heappop(a)
print(a[0])