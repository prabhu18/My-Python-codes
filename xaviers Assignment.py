__author__ = 'pjha'
x=input()
k=y=map(int,raw_input().split())

z=input()
pos=z
while(len(k)>1):
    while(pos<=len(k)):
        del k[pos-1]
        pos=pos+z-1


    pos=pos%len(k)
    del k[pos-1]
    pos=pos+z-1

print y,z
if(k[0]%2==0):
    y=filter(lambda a: a%2==0, y)
    print y.sort(reverse=True)
else:
    y=filter(lambda a: a%2!=0, y)
    print y.sort(reverse=True)



