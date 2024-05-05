n = int(input())
for i in range(n):
    a = input().split()
    for i in a:
        print(i[::-1],end=' ')
    print()