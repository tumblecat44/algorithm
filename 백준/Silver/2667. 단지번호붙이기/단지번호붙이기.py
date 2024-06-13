from collections import deque






n = int(input())
arr = [[] for _ in range(n)]
for i in range(n):
  arr[i] = (list(map(int,input())))

def bfs(i,j):
  q = deque([(i,j)])
  many = 0
  while q:
    x,y = q.popleft()
    for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
      nx,ny = x+dx,y+dy
      if 0<=nx<n and 0<=ny<n and visit[nx][ny]==0 and arr[nx][ny] == 1:
        q.append((nx, ny))
        visit[nx][ny] = True
        many +=1
  if many == 0:
    return 1
  else:
    return many

good = 0
res = []
visit = [[False for _ in range(n)] for _ in range(n)]
for i in range(n):
  for j in range(n):
    if visit[i][j] == False and arr[i][j]==1:
        good+=1
        res.append(bfs(i,j))
res.sort()
print(good)
for i in res:
  print(i)