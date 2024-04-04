a = input()
l = [0]*26
for i in range(len(a)):
    temp =(ord(a[i])-97)
    l[temp] += 1
print(*l)