n = int(input())
a = list(map(int, input().split()))
res = [0 for _ in range(n)]
stack = []
for q,i in reversed(list(enumerate(a))):
    while stack and a[stack[-1]] < i:
        res[stack.pop()] = q+1
    stack.append(q)
print(*res)