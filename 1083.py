a = int(input())
count = 0
for i in range(1, a + 1):
    b = i
    while (b != 0):
        c = b % 10
        if (c == 3 or c == 6 or c == 9):
            count += 1
        b = b // 10

    if (count == 0):
        print(i)
    else:
        for j in range(0, count):
            print("X", end="")
        print()
        count = 0
