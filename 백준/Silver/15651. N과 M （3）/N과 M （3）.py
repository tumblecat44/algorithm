def dfs():
    if len(s) == m:
        print(*s)

        return
    else:
        for i in range(1,n+1):

            s.append(i)
            dfs()
            s.pop()


h = []
n, m = map(int, input().split())
s = []

dfs()