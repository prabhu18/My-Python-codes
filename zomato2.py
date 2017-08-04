__author__ = 'pjha'
for i in range(0,input()):
    y=map(int,raw_input().split())
    gcd=y[0]
    num=y[1]
    A=[]
    if(gcd%2==0):
        for j in range(gcd+1,2*gcd+1):
            if(j%gcd==0):
                A.append(j)
    else:
        for j in range(gcd+1,3*gcd+1):
            if(j%gcd==0):
                A.append(j)

    for k in A:
        print k,
