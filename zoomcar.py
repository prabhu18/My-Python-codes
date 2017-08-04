__author__ = 'pjha'
x=input()
y=map(int,raw_input().split())
p=[]
for i in range(0,len(y)):
    s=0
    for j in y:
        if(y[i]%j==0 and y[i]!=j):
            s=1
    if(s==0):
        p.append(y[i])
for k in p:
    print k,

