x=input()
for i in range(0,x):
    z=map(int,raw_input().split())
    N=z[0]
    K=z[1]
    P=z[2]
    A=map(int,raw_input().split())


    d=1
    j=0
    while(d):
        count=0
        for m in A:
            if(m in (j-P,j+P)):

                count=count+1

            if(count>=K):
                d=0
                break;
        j=j+1

    if(d==0):
        print 'NO'

