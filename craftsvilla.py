__author__ = 'pjha'


x=input()
a=[]
s=0
for j in range(0,x):
    y=input()
    i=1
    sum=0
    s=0
    while(i<=y):
        if((i not in a) and (bin(i).count("1")==2)):
            a.append(i)
            s=1
            sum=sum+i

        if(i in a and s == 0):
            sum=sum+i
        i=i+1
    print sum

