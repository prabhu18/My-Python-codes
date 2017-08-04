def trailing_zeros(num):
    pnum = str(num)
    return len(pnum)-len(pnum.rstrip('0'))
def fact(n):
    if(n==0):
        return 1
    else:
        return n*fact(n-1)

x=input()
for i in range(0,x):
    a=map(int,raw_input().split())
    A=a[0]
    B=a[1]
    print trailing_zeros(fact(A)*fact(B))
	