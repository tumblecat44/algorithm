from collections import deque
import sys
T = int(sys.stdin.readline().strip())
c = deque()
for i in range(T):
    a =  sys.stdin.readline().split()
    if a[0] == "push_front":
        c.appendleft(int(a[1]))
    elif a[0] == "push_back":
        c.append(int(a[1]))
    elif a[0] == "pop_front":
        if c:
            print(c.popleft())
        else:
            print(-1)
    elif a[0] == "pop_back":
        if c:
            print(c.pop())
        else:
            print(-1)
    elif a[0] == "size":
        print(len(c))
    elif a[0] == "empty":
        if c:
            print(0)
        else:
            print(1)
    elif a[0] == "front":
        if c:
            print(c[0])
        else:
            print(-1)
    elif a[0] == "back":
        if c:
            print(c[-1])
        else:
            print(-1)