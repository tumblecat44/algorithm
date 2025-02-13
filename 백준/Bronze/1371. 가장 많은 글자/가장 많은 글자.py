import collections

a = []
try:
    while True:
        w = input().split()
        for i in w:
            for j in i:
                a.append(j)
except :
    pass
finally:
    counts = collections.Counter(a)
    ss = counts.most_common(1)[0][1]
    res = []
    for i in counts.items():
        if i[1] == ss:
            res.append(i[0])
    res.sort()
    for i in res:
        print(i,end='')