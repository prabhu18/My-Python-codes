__author__ = 'pjha'

def forloop(list):
    r = 1
    for x in list:
        r *= x
    return r

x=input()
y=map(int,raw_input().split())
for i in range(0,input()):
    k=input()
    z=forloop(y)

    v=[]
    flag=0
    c=0
    while(z!=0):

        if(z%k==0):
            v.append(0)
            z=z/k
            c=c+1
        else:
            break
    print c

