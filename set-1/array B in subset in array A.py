n,m=map(int, input().split())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]
count=0

for i in B:
    if i in A:
        count+=1
if(len(B) == count):
    print("YES")
else:
    print("NO")