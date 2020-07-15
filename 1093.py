array = [0 for i in range(23)]

count = int(input())

num = list(map(int,input().split()))
for i in range (0,count):
  array[num[i]-1] += 1

for i in array:
  print(i,end=" ")