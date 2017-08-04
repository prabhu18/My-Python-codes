__author__ = 'pjha'
x=input()

if(x%2!=0):
    x=x/2+1
    sum=x*(x+1)
    print sum - 1
else:
    x=x/2
    sum=x*(x+1)
    print sum+x