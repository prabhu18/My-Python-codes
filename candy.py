__author__ = 'pjha'
for j in range(0,input()):
    x=map(int,raw_input().split())
    N=x[0]
    C=x[1]
    M=x[2]
    ct=N/C
    ch=N/C

    while(ch/M!=0):
        ct=ct+ch/M
        d=ch/M
        ch=d+ch/M

    print ct


