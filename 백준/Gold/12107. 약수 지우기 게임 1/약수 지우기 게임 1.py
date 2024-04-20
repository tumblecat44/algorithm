t = int(input())
res = True
for i in range(1,t):
    if t%i==0:
        res = False
        break
if res:
    print("B")
else:
    print("A")