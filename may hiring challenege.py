__author__ = 'pjha'
x=input()
for i in range(0,x):
    y=input()
    z=map(int,raw_input().split())
    ma=max(z)
    k=1
    set=1
    while(set==1):
        m=0
        for j in z:
            if((ma*k)%j!=0):
                break;
            else:
                m=m+1
            if(m==len(z)):
                set=0
                break;
        if(set==0):
            break;
        else:
            k=k+1
    print ma*k