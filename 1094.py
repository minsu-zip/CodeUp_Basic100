num = int(input())
array = [0 for i in range(num)]
input = list(map(int, input().split()))
array = input
array.reverse()
for i in array:
  print(i,end=" ")