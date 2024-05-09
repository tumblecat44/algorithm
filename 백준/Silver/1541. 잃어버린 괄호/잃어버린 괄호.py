a = input()
m = a.split('-')
res = 0
if a[0]=='-':
    res-=sum(map(int,m[0].split('+')))
else:
    res+=sum(map(int,m[0].split('+')))
for i in m[1::]:
    res-=sum(map(int,i.split('+')))
print(res)
