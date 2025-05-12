from collections import deque
import sys
input = sys.stdin.readline
n,m = map(int,input().split())

graph = [[] for _ in range(n+1)]
degree = [0 for _ in range(n+1)]
res = []
for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    degree[b] += 1

q = deque([])
for i in range(1,n+1):
    if degree[i] == 0:
        q.append(i)

while q:
    nl = q.popleft()
    res.append(nl)
    for i in graph[nl]:
        degree[i] -= 1
        if degree[i] == 0:
            q.append(i)
print(*res)