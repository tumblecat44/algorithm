t = int(input())
a = [input() for i in range(t)]
big = 0
a.sort()
res = {}
for i in a:
    if a.count(i) > big:
        big = a.count(i)
        res[i] = a.count(i)
print(max(res.keys()))
