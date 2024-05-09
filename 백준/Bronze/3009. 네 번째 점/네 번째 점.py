a,b = map(int,input().split())
c,d = map(int,input().split())
e,f = map(int,input().split())
on = []
tw = []
on.extend([a,c,e])
tw.extend([b,d,f])
for i in range(3):
    if on.count(on[i]) == 1:
        print(on[i],end= ' ')
for i in range(3):
    if tw.count(tw[i]) == 1:
        print(tw[i])