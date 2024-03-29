t = int(input())
a = list(map(int,input().split()))
result = '^'.join(map(str, a))
if eval(result) == 0:
    print("cubelover")
else:
    print("koosaga")