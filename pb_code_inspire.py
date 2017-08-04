__author__ = 'pjha'
for i in range(0,input()):
    y=input()
    x=map(int,raw_input().split())
    j=0
    set=0
    while(x[j]!=y):
        k=x[j]-1
        x[j]=9999999
        j=k
        if(x[j]==9999999):
            set=1
            break
    if(set==0):
        print 'YES'
    else:
        print 'NO'

