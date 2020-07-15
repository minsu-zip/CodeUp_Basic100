array = [[0 for j in range(19)] for i in range(19)]

for i in range(0, 19):
    inputlist = list(map(int, input().split()))
    for j in range(0, 19):
        array[i][j] = inputlist[j]

count = int(input())
for i in range(0, count):
    x, y = map(int, input().split())
    for o in range(0, 19):
        if (array[x - 1][o] == 0):
            array[x - 1][o] = 1
        else:
            array[x - 1][o] = 0

        if (array[o][y - 1] == 0):
            array[o][y - 1] = 1
        else:
            array[o][y - 1] = 0

for k in array:
    for l in k:
        print(l, end=" ")
    print()
