import sys
N,M = map(int,sys.stdin.readline().strip().split())
k = list(map(int,sys.stdin.readline().strip().split()))
smuk = [0]*(N+1)
for i in range(1,N+1):
    smuk[i] = smuk[i-1]+k[i-1]
def ok(i,j):
    return smuk[j] - smuk[i-1]
for i in range(M):
    a,b = map(int,sys.stdin.readline().strip().split())
    print(ok(a,b))