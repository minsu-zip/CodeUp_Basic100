h,b,c,s= map(int,input().split())
sum = (h * b * c * s) / 8 / 1024 / 1024
print("%0.1f MB" %sum)