N = int(input())
l = int(input())
two = abs(100 - N)
if l == 0:
    print(min(two,len(str(N))))
else:


    a = list(map(int, input().split()))
    if l == 10:
        print(abs(N-100))
    elif N ==0:

        res = 0
        dd = 0
        for i in range(0,10):
            if i not in a:
                dd = i
                break
        for z in range(dd,0,-1):
            res+=1
        print(res+1)
    else:
        small = N+500
        res = 0

        for i in range(10**6):
            b = True
            for z in str(i):
                if int(z) in a:
                    b = False
                    break
            if b:
                if abs(i - N) < small:
                    small = abs(i - N)
                    res = i
        print(min(small + len(str(res)), two))