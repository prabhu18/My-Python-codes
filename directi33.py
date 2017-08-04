__author__ = 'pjha'
import re
x=raw_input()
y=input()
count=0
a=map(int,re.findall('\d+', x))
strx=''
final=''
k=0
n=0
for j in range(0,len(a)):

    final=''
    l=0
    while(x[k].isdigit()!=True):
        strx=strx+x[k]
        k=k+1
        l=l+1

    if(x[k].isdigit()):
        for m in range(0,a[n]):
            final=final+strx
        n=n+1
    v=a[n-1]
    k=(k*v)
    l=l+len(str(v))
    strx=final
    x=final+x[l:len(x)]
    print final,x



print final[y-1],final
