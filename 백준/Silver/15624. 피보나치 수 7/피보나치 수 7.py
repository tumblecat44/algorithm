n = int(input())
a,b = 1, 2
if n == 0:
    print(0)
elif n == 1:
    print(a)
elif n== 2:
    print(a)
else:
    for i in range(3, n+1):
        a,b = b%1000000007, (a+b)%1000000007
    print(a)