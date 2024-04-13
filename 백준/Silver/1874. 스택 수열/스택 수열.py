import sys
input = sys.stdin.readline
t = int(input())
a = list(map(int, [input() for i in range(t)])) #입력 받기
res = [0] #스택에 저장하기
z = 1 #스택에 추가되는 값
q = []# pop 한거 저장
ok = False # "NO" 인지 확인
for i in a:
    if ok:
        break
    else:
        while True:
            if res[-1] == i:
                q.append('-')
                res.pop()
                break
            if z> i*2:
                ok = True
                break
            res.append(z)
            z+=1
            q.append('+')

if ok:
    print("NO")
else:
    for i in q:
        print(i)