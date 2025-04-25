n = int(input())
def dfs(x):
    if x not in res:
        res.append(x)
    one = int(str(x)[-1])
    for w in range(one-1,-1,-1):
        dfs(x*10 +w)
res = []
for i in range(0,10):
    dfs(i)
res.sort()
if n >= len(res):
    print(-1)
else:
    print(res[n])