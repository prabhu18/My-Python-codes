__author__ = 'pjha'

x='5#9#6#4#6#8#0#7#1#5'
y=list(x)
y=filter(lambda a: a != '#', y)
j=0
k=[]
while(j<len(y)):
    k.append(int(y[j]))
    j=j+1
print k
maxi=0
i=0
j=1
n=1
while(j<=len(k)):
    m=[]
    m=k[i:j]
    maxi=maxi+max(k)
    i=j
    n=n+1
    j=j+n
    print m
print maxi









