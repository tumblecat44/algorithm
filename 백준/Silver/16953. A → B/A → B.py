a,b = map(int,input().split())
result = 1
while b != a:
    result+=1
    no = b
    if b%10 ==1:
        b = b//10
    elif b%2 == 0:
        b = b//2
    if no == b:
        print(-1)
        break
else:
    print(result)