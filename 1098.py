height, width = map(int, input().split())
array = [[0 for j in range (width)] for i in range(height)]
number = int(input())

for i in range (number):
  l,d,x,y = map(int, input().split())
  if d == 0:
    for j in range (l):
      array[x-1][y-1 + j] = 1
  else :
    for k in range (l):
      array[x-1 + k][y-1] = 1


for i in array:
  for j in i:
    print(j, end=" ")
  print()
