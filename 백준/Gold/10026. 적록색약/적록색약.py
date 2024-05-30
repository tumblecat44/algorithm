from collections import deque

n = int(input())
area = []
for i in range(n):
    area.append(list(input()))
visit = [[False for _ in range(n)] for _ in range(n)]


# 적록색약 아님
def bfs(l):
    q = deque([(l)])
    while q:
        x,y = q.popleft()
        for i,j in ((0,1),(1,0),(-1,0),(0,-1)):
            nx,ny = x+i,y+j
            if 0<=nx<n and 0<=ny<n and area[nx][ny]==area[x][y] and visit[nx][ny] == False:
                q.append((nx,ny))
                visit[nx][ny] = True
no = 0
for i in range(n):
    for j in range(n):
        if visit[i][j] == False:
            bfs((i,j))
            no+=1

# 적록색약
visit = [[False for _ in range(n)] for _ in range(n)]
def ybfs(l):
    q = deque([(l)])
    while q:
        x,y = q.popleft()
        for i,j in ((0,1),(1,0),(-1,0),(0,-1)):
            nx,ny = x+i,y+j
            if 0<=nx<n and 0<=ny<n and (area[nx][ny]==area[x][y] or ((area[nx][ny] == 'R' and area[x][y] == 'G'))or(area[nx][ny] == 'G' and area[x][y] == 'R')  ) and visit[nx][ny] == False:
                q.append((nx,ny))
                visit[nx][ny] = True
yes = 0
for i in range(n):
    for j in range(n):
        if visit[i][j] == False:
            ybfs((i,j))
            yes+=1
print(no,yes)