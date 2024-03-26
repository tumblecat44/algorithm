import sys
a,b = map(int,sys.stdin.readline().strip().split())
p = {}
c = []
for k in range(1,a+1):
    z = sys.stdin.readline().strip()
    p[z] = k
re_p = dict(map(reversed,p.items()))
for i in range(b):
    o = sys.stdin.readline().strip()
    if o.isdigit():
        c.append(re_p[int(o)])
    else:
        c.append(p[o])
for i in range(b):
    print(c[i])