n=int(input())
l=[int(i) for i in input().split()]
s=""
for i,j in enumerate(l):
    if(i%2!=0 and j%2==0 or i%2==0 and j%2!=0):
        s=s+str(j)+" "
print(s)