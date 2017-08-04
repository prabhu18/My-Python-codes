__author__ = 'pjha'
for i in range(0,input()):
    x=map(int,raw_input().split())
    N=x[0]
    K=x[1]
    S=[]
    P=[]
    for j in range(0,K):
        S.append(map(int,raw_input().split()))

    for k in S:
        P.append(sum(k))
    print P




