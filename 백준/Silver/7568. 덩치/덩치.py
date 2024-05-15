n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
for i in a:
    q = 1
    for j in range(n):
        if a[j][0] > i[0] and a[j][1] > i[1]:
            q += 1
    print(q,end=' ')