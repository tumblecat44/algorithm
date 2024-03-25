from collections import deque
N = int(input())
dq = deque(i for i in range(1,N+1))
for i in range(N-1):
    dq.popleft()
    dq.append(dq[0])
    dq.popleft()
print(*dq)