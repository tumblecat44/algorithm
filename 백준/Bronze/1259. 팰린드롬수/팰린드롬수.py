res = 1
while res != 0:
    a = input()
    if a == "0":
        break
    if a == a[::-1]:
        print("yes")
    else:
        print("no")