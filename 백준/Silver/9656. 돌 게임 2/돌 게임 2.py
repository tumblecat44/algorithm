def solve(i):
    if i == 2:
        return "SK"
    elif i == 1 or i==3:
        return "CY"
    else:
        if i%2 == 1:
            return "CY"
        else:
            return "SK"
    
a = int(input())
print(solve(a))