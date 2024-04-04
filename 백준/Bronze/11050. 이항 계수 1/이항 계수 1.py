import math
n,k = map(int,input().split())
pac = math.factorial 
print(int(pac(n)/(pac(n-k)*pac(k))))