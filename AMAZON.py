from fractions import gcd

def F(x):
    sum=0
    a=1
    b=x
    while(a<=b):
        sum=sum+gcd(a,x)
        a=a+1


    return sum



x=input()
y=map(int,raw_input().split())
for j in range(0,input()):
    t=raw_input().split()
    sum=0
    if(t[0]=='C'):
        a=int(t[1])
        b=int(t[2])
        sum=0
        while(a<=b):
            sum=sum+F(y[a-1])
            a=a+1
        print sum
    else:

        a=int(t[1])
        b=int(t[2])
        y[a-1]=b
