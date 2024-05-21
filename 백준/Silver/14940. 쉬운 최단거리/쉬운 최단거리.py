from collections import deque
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
res = [[-1 for _ in range(m)] for _ in range(n)]
def bfs(i,j):
    q = deque([(i,j)])
    visit = [[False for _ in range(m)] for _ in range(n)]
    while q:
        x,y = q.popleft()
        for i in ((0,1),(1,0),(-1,0),(0,-1)):
            dx,dy = x+i[0],y+i[1]
            if 0<=dx<n and 0<=dy<m and a[dx][dy]==1 and not visit[dx][dy]:
                visit[dx][dy] = True
                q.append((dx,dy))
                res[dx][dy] = res[x][y] + 1

for i in range(n):
    for j in range(m):
        if a[i][j] == 2:
            y,u = i,j
        if a[i][j] == 0:
            res[i][j] = 0
res[y][u] = 0
bfs(y,u)
for i in res:
    print(*i)