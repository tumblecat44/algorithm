a,b,c = map(int,input().split())
if a == b == c:
    print(10000 + (1000*a))
elif a == b or a == c or b == c:
    if a == b:
        print(1000 + (a*100))
    elif a == c:
        print(1000 + (a*100))
    elif c == b:
        print(1000 + (c*100))
else:
    numlist = [a,b,c]
    print(max(numlist)* 100)