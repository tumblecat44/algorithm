t = int(input())
def solve():
    a = list(map(int,input().split()))
    s = a[0]
    a.remove(a[0]) 
    c = sum(a)/s
    res = 0
    for i in a:
        if i > c:
            res+=1
    print("%.3f%%"%(res/s*100))

for i in range(t):
    solve()