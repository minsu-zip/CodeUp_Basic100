a,b = input().split()
a = int(a)
b = int(b)
print(  (a & b) | int((not(a)) & (not(b))))