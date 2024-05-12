from collections import deque
n,m = map(int,input().split())
maps = [input() for i in range(n)]
def bfs(x,y):
    q = deque()
    q.append((x,y))
    res= 0
    visit = [[False for i in range(m)] for i in range(n)]
    while q:
        x,y = q.popleft()
        for i in ((-1,0),(1,0),(0,1),(0,-1)):
            nx,ny = x+i[0], y+i[1]
            if 0<=nx<n and 0<=ny<m and  maps[nx][ny] != "X" and visit[nx][ny] != True:
                if maps[nx][ny] == "P":
                    res+=1
                q.append((nx,ny))
                visit[nx][ny] = True
    return res if res !=0 else "TT"
for i in range(n):
    for j in range(m):
        if maps[i][j]== 'I':
            print(bfs(i,j))