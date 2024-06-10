a,b = map(int,input().split())
kim = [0]*a
for i in range(b):
    c,d,e = map(int,input().split())
    for k in range(c,d+1):
        kim[k-1] = e
for i in range(a):
    print(kim[i],end=' ')