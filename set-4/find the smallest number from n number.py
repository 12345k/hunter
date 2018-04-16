import itertools
c=0
n=str(input())
l=[]
for subset in itertools.permutations(n,len(n)):
     a="".join(subset)
     l.append(int(a))
l.remove(int(n))
print (min(l))
if(min(l)>int(n)):
    print (min(l))
else:
    print ("impossible")