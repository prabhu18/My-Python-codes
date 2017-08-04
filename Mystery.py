__author__ = 'pjha'

x=input()
for i in range(0,x):
	q=raw_input().split()
	S=q[0]
	V=int(q[1])

	L=list(S)
	A=[]
	for j in L:
		val=ord(j)+V
		if(val<=122):
			A.append(chr(val))

		if(val>122):
			d=val-122
			A.append(chr(96+d))

	print ''.join(A)