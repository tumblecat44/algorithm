import sys
input = sys.stdin.readline
n,m = map(int,input().split())
chess = []
count = []
for _ in range(n):
    chess.append(input().strip())
for i in range(n-7):
    for k in range(m-7):
        w_count = 0
        b_count = 0
        for ni in range(i,i+8):
            for nk in range(k,k+8):
                if (ni + nk)%2 == 0:
                    if chess[ni][nk] != 'W':
                        w_count += 1
                    if chess[ni][nk] != 'B':
                        b_count +=1
                else:
                    if chess[ni][nk] != 'B':
                        w_count+=1
                    if chess[ni][nk] != 'W':
                        b_count+=1
        count.append(min(w_count,b_count))
print(min(count))