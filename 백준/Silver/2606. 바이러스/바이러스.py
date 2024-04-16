import sys
input = sys.stdin.readline

res = []
def dfs(idx):
    global visited
    visited[idx] = True
    res.append(idx)
    for i in range(1,N+1):
        if not visited[i] and graph[i][idx]:
            dfs(i)

N = int(input())
M = int(input())
graph = [[False]*(N+1) for _ in range(N+1)]
visited = [False]*(N+1)

for _ in range (M):
    a,b = map(int,input().split())
    graph[a][b] = True
    graph[b][a] = True
dfs(1)
print(len(res)-1)