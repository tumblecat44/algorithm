while True:
    a = list(map(int,input().split()))
    if a == [0,0,0]:
        break
    c = max(a)**2
    a.remove(max(a))
    if a[0]**2 + a[1]**2 == c:
        print("right")
    else:
        print("wrong")