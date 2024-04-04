import math
t = int(input())
pac = math.factorial
for i in range(t):
    k,n = map(int,input().split())
    print(int(pac(n)/(pac(n-k)*pac(k))))