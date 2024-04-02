n = int(input())
res = 0
while True:
    if n%5== 0:
        res += n//5
        break
    else:
        
        if n-3 <0:
            res= -1
            break
        else:
            res+=1
            n-=3
print(res)