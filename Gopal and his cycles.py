__author__ = 'pjha'

x=input()
for i in range(0,x):
    s=map(int,raw_input().split())
    A=s[0]
    B=s[1]
    count=0
    if( (A==B/2) or (B==A/2) or (A==2*B+1) or (B==2*A+1)):
            count=count+1

    else:
        while(A!=B):

                if(A!=1):
                    A=A/2
                    count=count+1
                if(B!=1):
                    B=B/2
                    count=count+1
    print count+1