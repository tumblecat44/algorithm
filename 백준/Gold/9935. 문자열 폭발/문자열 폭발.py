a = input()
boom = input()
stack = []
c = len(boom)
for i in a:
    stack.append(i)
    while len(stack) >= c and "".join(stack[-c:]) == boom:
        for j in range(c):
            stack.pop()
if stack:
    print("".join(stack))
else:
    print("FRULA")