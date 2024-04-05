from collections import deque
import sys
T = int(sys.stdin.readline().strip())
c = []
for i in range(T):
    a =  sys.stdin.readline().split()
    if a[0] == "push":
        c.append(a[1])
    elif a[0] =='pop':
        if c:
            print(c.pop())
        else:
            print(-1)
    elif a[0] == 'size':
        print(len(c))
    elif a[0] == 'empty':
        if c:
            print(0)
        else:
            print(1)
    elif a[0] == "top":
        if c:
            print(c[-1])
        else:
            print(-1)