a,b,c=input().split()
R=int(a)
G=int(b)
B=int(c)
c=0
for i in range(R) :
    for j in range(G) :
        for k in range(B) :
            c+=1
            print(i, j, k)

print(c)