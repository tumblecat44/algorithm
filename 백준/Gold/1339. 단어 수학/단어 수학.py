n = int(input())
t = [input() for _ in range(n)]
a = []
for i in t:
    a.append(i)
now = 9
res = {}
while a:
    w = a.index(max(a, key=len))
    q = a.pop(w)
    if q:
        if q[0] in res:
            res[q[0]] = res[q[0]] + int(("1" + ("0"*len(q))))
            # now -= 1
        else:
            res[q[0]] = int(("1" + ("0" * len(q))))
        q = q[1:]
        if q:
            a.append(q)
# print(res)
sorted_dict = dict(sorted(res.items(), key=lambda item: item[1], reverse=True))
# print(sorted_dict)
real = {}
for i in sorted_dict:
    real[i] = now
    now-=1
# print(real)
ss = []
for i in t:
    ww = []
    for j in i:
        ww.append(real[j])
    ss.append(int("".join(map(str,ww))))
print(sum(ss))
