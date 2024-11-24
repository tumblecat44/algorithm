r=0;n=int(input())
for _ in' '*n:s=[];[s.pop()if s and s[-1]==c else s.append(c)for c in input()];r+=not s
print(r)