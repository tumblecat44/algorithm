def dfs(st):
    if len(s) == m:
        print(*s)

        return
    else:
        for i in range(st,n+1):
            if i not in s:
                s.append(i)
                dfs(i+1)
                s.pop()


h = []
n, m = map(int, input().split())
s = []

dfs(1)