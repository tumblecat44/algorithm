import sys
from collections import Counter
T = int(sys.stdin.readline().strip())
res = []
for i in range(T):
    s = list(sys.stdin.readline().strip().split("."))
    res.append(s[1])
a = Counter(res)
sort_a = sorted(a.items())
for z,k in sort_a:
    print(z,k)