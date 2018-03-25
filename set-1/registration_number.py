print("Total no.of registration number:")
n=int(input())#n number
l=[]
duplicate = []
for i in range(n):
    reg = int(input())
    if reg not in l:
        l.append(reg)
    else:
        duplicate.append(reg)
if(len(duplicate)==0):
    print("No repeated number")
else:
    print("The repeated numbers are")
    for i in duplicate:
        print(i)