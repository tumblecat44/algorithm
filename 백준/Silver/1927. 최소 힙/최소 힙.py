import heapq
import sys

input = sys.stdin.readline
N = int(input())
heap = []
for i in range(N):
    s = int(input())
    if s:
        heapq.heappush(heap,s)
    else:
        if heap:
            res = heapq.heappop(heap)
            print(res)
        else:
            print(0)
