def hamming2(s1, s2):
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))

x=input()
for i in range(0,x):
	a=map(int,raw_input().split())
	A=bin(a[0])
	B=bin(a[1])
	print hamming2(A,B)
	
	
