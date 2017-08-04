__author__ = 'pjha'
for i in range(0,input()):
    x=map(int,raw_input().split())
    N=x[0]
    M=x[1]
    L=[]
    R=[]
    C=[]
    y=map(int,raw_input().split())
    L[0]=y[0]
    R[0]=y[1]
    C[0]=y[2]
    P=y[3]
    Q=y[4]
    S=y[5]

    Ins=[0]*N
    L[i] = (L[i-1] * P + R[i-1]) % N + 1
    R[i] = (R[i-1] * Q + L[i-1]) % N + 1
    if(L[i] > R[i]):
        L[i] ,R[i]= R[i],L[i]
    C[i] = (C[i-1] * S) % 1000000 + 1
    p=L[i]
    for j in range(0,M):
        while(p<=R[i]):
            Ins[p-1]=C[j]
    print Ins