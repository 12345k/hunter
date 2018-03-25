import itertools
l = [int(i) for i in input().split()]
m = list(itertools.permutations(l))
s=""
num=(m[-1])
for i in num:
    s=s+str(i)
print(s)

