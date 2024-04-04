n = int(input())
a = set(map(int,input().split()))
z = int(input())
k = list(map(int,input().split()))
for i in k:
    if i in a:
        print(1)
    else:
        print(0)