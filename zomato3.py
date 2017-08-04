__author__ = 'pjha'
for i in range(0,input()):
    y=map(int,raw_input().split())
    N=y[0]
    K=y[1]
    M=y[2]
    A=[]
    for j in range(0,N):
        A.append(raw_input())

    A = sorted(A, key = lambda x: (x[0:3]))
    print A[K-1]
