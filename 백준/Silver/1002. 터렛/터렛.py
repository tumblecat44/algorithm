from math import sqrt
def solve():
    x,y,r,x1,y1,r1 = map(int,input().split())
    dist = sqrt((x-x1)**2 + (y-y1)**2)
    diff = abs(r-r1)
    ans = 0
    if dist == 0 and r == r1:
        ans =-1
    elif dist == r+r1 or dist == diff:
        ans = 1
    elif diff < dist < r+r1:
        ans = 2
    print(ans)
T = int(input())
for i in range(T):
    solve()