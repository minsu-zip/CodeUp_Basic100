a = input()
number = len(a) - 1
for i in a:
    print("[" + i, end="")
    for j in range(number, 0, -1):
        print(0, end="")
    number = number - 1
    print("]")
