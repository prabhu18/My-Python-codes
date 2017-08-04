n=str(raw_input())
l=list(n)
g=[]
d=len(l)-1
while d>=0:
	g.append(l[d])
	d=d-1
cnt=0
for i in range(len(g)):
		if l[i]==g[i]:
			cnt=cnt+1
		else:
			cnt=cnt-1
if len(list(set(l)))== 1 :
    print 1
else:
    if cnt==len(g):
        print "%d"%((len(g)-1))
    else:
        print "%d"%(len(g))