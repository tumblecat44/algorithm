import math
import sys
n = int(input())
start = 1
end = 10**6
while start <= end:
    mid = (start+end)//2
    q = math.factorial(mid)
    if q == n:
        print(mid)
        sys.exit()
    elif q < n:
        start = mid + 1
    else:
        end = mid - 1
