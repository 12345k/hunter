l = [int(i) for i in input().split(",")]#get the input
m=[]
n=len(l)#find the length
for i in range (0,n):
    d=l.count(l[i])#count the number of times variable occured
    if d==1:#unique condition
        m.append(l[i])

print(m)#output