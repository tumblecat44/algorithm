Namegi = input()
um =  Namegi.split(" ")
A = int(um[0])
B = int(um[1])


if A < B:
    print("<")
elif A > B:
    print(">")
elif A == B:
    print("==")