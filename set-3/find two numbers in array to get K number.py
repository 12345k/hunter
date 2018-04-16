n,k=map(int,input().split())
l=[int(i) for i in input().split()]
c=0
for i,j in enumerate(l):
    if k-i in l:
        c=1
        print("YES")
        break
if(c==0):
    print("NO")
