import sys
input = sys.stdin.readline

def dfs(idx):
    global visited
    visited[idx] = True
    print(idx,end=' ')
    for i in range(1,N+1):
        if not visited[i] and graph[i][idx]:
            dfs(i)
def bfs():
    global visited,q
    while q:
        idx = q.pop(0)
        print(idx,end=' ')
        for i in range(1,N+1):
            if not visited[i] and graph[i][idx]:
                visited[i] = True
                q.append(i)

N,M,V = map(int,input().split())
graph = [[False]*(N+1) for _ in range(N+1)]
visited = [False]*(N+1)

for _ in range (M):
    a,b = map(int,input().split())
    graph[a][b] = True
    graph[b][a] = True
dfs(V)
print()
visited = [False]*(N+1)
q = [V]
visited[V] = True
bfs()
