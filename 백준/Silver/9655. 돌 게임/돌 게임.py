def solve(i):
    if i == 2:
        return "CY"
    elif i == 1 or i==3:
        return "SK"
    else:
        if i%2 == 1:
            return "SK"
        else:
            return "CY"
    
a = int(input())
print(solve(a))