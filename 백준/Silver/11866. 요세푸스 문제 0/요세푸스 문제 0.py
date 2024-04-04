from collections import deque
n,k = map(int,input().split())
res = deque(range(1,n+1))
z = []
while res:
    a =1
    while a <k:
        t = res.popleft()
        res.append(t)
        a +=1
    c = res.popleft()
    z.append(c)
print("<",end='')
print(*z,sep=', ',end='')
print(">")