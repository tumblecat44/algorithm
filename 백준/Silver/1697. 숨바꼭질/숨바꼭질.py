from collections import deque
n,k = map(int,input().split())
q = deque()
visit = [False for _ in range(10000001)]
q.append([n,0])
while q:
    a = q.popleft()
    if a[0] == k:
        print(a[1])
        break
    if a[0] < 100001:
        if not visit[a[0]]:
            visit[a[0]] = True
            q.append([a[0] + 1, a[1] + 1])
            q.append([a[0] - 1, a[1] + 1])
            q.append([a[0]*2, a[1]+1])


