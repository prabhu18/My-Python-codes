__author__ = 'pjha'

x=input()
y=input()
i=1
z=0
w=0
count=0
while(i<=y):
    z=z+str(i).count('4')
    w=w+str(i).count('7')
    if((z+w)>x):
        count=count+1
        z=0
        w=0
    i=i+1
print count