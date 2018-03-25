l = [int(i) for i in input().split()]

for i in l:
    if(l.count(i)>1):
        print("The first element repeated is:",i)
        break
