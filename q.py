a=input()
A=[]
for i in range(0,a):
	A.append(i+1)

s=raw_input()
S=list(s)
i=0
val=0
while(len(A)>1):
    i=0
    s=0
    for j in S:

        if(j=='a' and i<len(A)-1 and s==0):
            val=i+1
            s=1

        if(j=='b' and i<len(A)-1 and s==0):
            val=i+1
            A.remove(j)
            s=1

        if(j=='a' and i<=len(A)-1 and s==0):
            val=0
            s=1

        if(j=='b' and i<=len(A)-1 and s==0):
            val=0
            A.remove(j)
            s=1
print A[0]



__author__ = 'pjha'
