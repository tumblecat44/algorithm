c = []
for i in range(5):
    c.append(int(input()))
c.sort()
print(int(sum(c)/5))
print(c[2])