n = int(input())
n += 1
res = str(bin(n)[2:])
res = res.replace("0","4")
res = res.replace("1","7")
print(res[1:])