import numpy as np
n,k=map(int,input().split())
l=[]
for i in range(n):
    s=[int(i) for i in input().split()]
    l.append(s)
l=list(np.concatenate(l))
set_l = list(set(l))
s=""
for i in set_l:
    # print(l.count(i))
    if(l.count(i)>=n):
        s+=str(i)+" "
print(s)