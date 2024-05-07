from collections import deque
n,m = map(int,input().split())
maze = []
for i in range(n):
    maze.append(list(map(int,input())))

def bfs(x,y):
    q = deque()
    q.append((x,y))
    while q:
        x,y = q.popleft()
        for i in ((-1,0),(1,0),(0,1),(0,-1)):
            nx,ny = x+i[0], y+i[1]
            if 0<=nx<n and 0<=ny<m and  maze[nx][ny]==1:
                maze[nx][ny]= maze[x][y]+1
                q.append((nx,ny))
    return maze[n-1][m-1]
print(bfs(0,0))