input1 = int(input())
array = [[0 for i in range(19)] for j in range(19)]

for i in range (0,input1):
  a,b = map(int, input().split())
  array[a-1][b-1] = 1

for x in array:
  for y in x:
    print(y, end=" ")
  print()
