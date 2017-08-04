x=input()
for i in range(0,x):
	a=map(int,raw_input().split())
	A=a[0]
	B=a[1]
	C=a[2]
	K=a[3]
	j=0
	M=[]
	while( (A*j*j+B*j+C)<=K ):

		if(j==0 and A*j*j+B*j+C==K):
			M.append(0)
			j=j+1
		else:
			j=j+1

			M.append(j)


	try:
		print max(M)
	except:
		print 0