x = int(input())

def check(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def solve(n):
    if len(str(n)) == x:
        print(n)
    for i in range(1,10,2):
        if check(n * 10 + i):
            solve(n * 10 + i)

solve(2)
solve(3)
solve(5)
solve(7)