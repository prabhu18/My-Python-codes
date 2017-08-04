x=input()
a=map(int,raw_input().split())
b=map(int,raw_input().split())
A=[]

for i in range(0,a[0]):
	A.append(b[i])

print A,b[a[0]-1],len(b)
for j in range(a[1]-1,len(b)):
	if(A.__contains__(b[j])):
		print 'YES'
	else:
		print 'NO'
        A.append(b[j])