array = [[0 for j in range(10)] for i in range(10)]

for i in range (10):
  inputlist = list(map(int, input().split()))
  for j in range (10):
    array[i][j] = inputlist[j]

check = True;
k=1

for i in range(1,10):
    if check == False:
      break
    else:
      for j in range(k,10):
        if array[i][j] == 1:
          if array[i+1][j-1] == 1:
            check = False
            break
          k = j - 1
          break
        elif array[i][j] == 2:
          array[i][j] = 9
          check = False
          break;
        else :
          array[i][j] = 9

for i in array:
  for j in i:
    print(j,end = " ")
  print()
