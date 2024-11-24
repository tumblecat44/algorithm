n = int(input())
res = 0
for i in range(n):
    a = list(input())
    stack = []
    qe = True
    for j in a:
        stack.append(j)
        if len(stack) >= 2:
            if stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()

    if len(stack) == 0:
        res += 1
print(res)