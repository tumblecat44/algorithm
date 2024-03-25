import sys
a,b = map(int,sys.stdin.readline().strip().split())
p = []
res = 0
for _ in range(a):
    z = int(sys.stdin.readline())
    p.append(z)
p.reverse()
while True:
    if b ==0:
        break
    for i in range(a):
        if b < p[i]:
            p.remove(p[i])
        if b>=p[i]:
            res +=b//p[i]
            b%=p[i]
            
            break
print(res)