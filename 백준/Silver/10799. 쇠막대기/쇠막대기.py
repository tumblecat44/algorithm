a = input()
stack = []
res = 0
for i in range(len(a)):
    if a[i] == "(":
        stack.append("(")
    else:
        stack.pop()
        if a[i-1]=="(":
            res+=len(stack)
        else:
            res += 1
print(res)