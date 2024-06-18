s,b = map(int,input().split())
a = [True]* (b-s+1)
no = []
for i in range(2,int(b**0.5)+1):
    z = i*i
    start = max(z, (s + z - 1) // z * z)
    for j in range(start, b + 1, z):
        a[j - s] = False
res = 0
for i in a:
    if i:
        res+=1
print(res)