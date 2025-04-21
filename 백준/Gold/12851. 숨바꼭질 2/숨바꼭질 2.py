import collections

n, k = map(int, input().split())
q = collections.deque([n])
big = 0
res = 0
way = [0 for _ in range(10000001)]

while q:
    a = q.popleft()
    w = way[a]
    if a == k:
        big = w
        res+=1
        continue

    for i in [a-1,a+1,a*2]:
        if 0 <= i < 100001 and (way[i] == 0 or way[i] == way[a] + 1):
            q.append(i)
            way[i] = way[a] + 1

print(big)
print(res)