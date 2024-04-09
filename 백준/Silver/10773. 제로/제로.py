from collections import deque
import sys
T = int(input())
c = deque()
for i in range(T):
    a = int(sys.stdin.readline())
    if a == 0:
        c.pop()
    else:
        c.append(a)
print(sum(c))