n = int(input())
check = '369'
rest = 0
for i in range(1,n+1):
    res = str(i)
    for z in check:
        rest+=res.count(z)
print(rest)