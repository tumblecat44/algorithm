import sys
input = sys.stdin.readline
n = int(input())
for i in range(n):
    a,b = input().upper().split()
    print(b[a.find('X')],end="")