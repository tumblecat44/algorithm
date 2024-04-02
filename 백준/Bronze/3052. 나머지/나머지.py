kim = []
kim = list(set(kim))
for i in range(10):
    a = int(input())%42
    if a not in kim:
        kim.append(a)
print(len(kim))