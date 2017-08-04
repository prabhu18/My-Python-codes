__author__ = 'pjha'
import re
x=raw_input()
y=input()
count=0
a=re.findall('\d+', x)
strx=''
k=0
n=0

for j in range(0,len(a)):
    final=''
    strx=''
    k=0


    while(x[k].isdigit()!=True):
        strx=strx+x[k]
        k=k+1


    if(x[k].isdigit()):
        for m in range(0,int(a[n])):
            final=final+strx
        n=n+1
    v=a[n-1]
    k=k+len(str(v))

    x=final+x[k:len(x)]


print x[y-1]
