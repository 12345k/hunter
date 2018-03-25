n= int(input())
pos=[]
neg=[]
l=[int(i) for i in input().split()]
for i in l:
    if(i>=0):
        pos.append(i)
    else:
        neg.append(i)
for i in neg:
    if abs(i) in pos:
        print(i,abs(i))
if pos.count(0) >=2:
    print("0 0")