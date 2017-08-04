x=input()
for i in range(0,x):
    a=map(int,raw_input().split())

    N=a[0]
    P=a[1]
    K=a[2]
    j=1
    A=[]
    m=0
    A=[1]
    while((A.__contains__(j+P) is False ) ):

        if(j+P<=N):
            A.append(j+P)
            j=j+P
        else:
            A.append(j+P-N)
            j=j+P-N

    A.sort()

    print A[K]





