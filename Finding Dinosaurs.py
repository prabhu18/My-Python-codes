x=map(int,raw_input().split())
A={}
for i in range(0,x[0]):
	c=map(str,raw_input().split())
	A[c[0]]=c[1]+c[2]+c[3]


for j in range(0,x[3]):
    B=map(str,raw_input().split())
    v=B[0]+B[1]+B[2]
    s=0
    if(A.values().__contains__(v)):

        for name, age in A.iteritems():
            if age == v:
                print name
                break
    else:
        print 'You cant fool me :P'



