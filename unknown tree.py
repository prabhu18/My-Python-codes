from itertools import groupby
x=[]
n=input()
for _ in xrange(n):
	x.append(raw_input())
c=0
a=[list(g) for m, g in groupby(x, key=lambda x: x[0])]
print a
for i in a:

    c+=len(set(''.join(j for j in i)))
print c+1