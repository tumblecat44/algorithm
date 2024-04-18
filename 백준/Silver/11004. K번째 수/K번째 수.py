a,b = map(int,input().split())
z = list(map(int,input().split()))
z.sort()
z = z[0:b]
print(z[-1])