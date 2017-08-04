def fib_to(n,x,y):
    fibs=[]
    for i in range(0,x):
        fibs.append(y)

    if(len(fibs)==2):
        fibs.append(fibs[-1]+fibs[-2])
    for j in range(x, n):
        fibs.append(fibs[-1] + fibs[-2]+fibs[-3])
    return fibs
		
x=input()
for i in range(0,x):
    a=map(int,raw_input().split())
    X=a[0]
    Y=a[1]
    N=a[2]
    A=fib_to(N,X,Y)
    print A
    print A[N-1]