a = int(input())
res = 1
zero = 0
for i in range(1,a+1):
    res*=i
for i in range(1,len(str(res))+1):
    k = -1*i
    if str(res)[k] != "0":
        zero = i-1
        break
    else:
        pass
print(zero)