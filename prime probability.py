__author__ = 'pjha'

def count_prime(a,b):
    num=a
    count=0
    while(a<=b):
        if(num>1):
            i=2
            while(i<num):
                if(num%i==0):
                    break
                else:
                    count=count+1
                i=i+1
        a=a+1

    return  count




x=input()
for i in range(0,x):
    y=map(int,raw_input().split())
    st=y[0]
    en=y[1]
    val=en-st+1
    count=count_prime(st,en)
    print count,val


