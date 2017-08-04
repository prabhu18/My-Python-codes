x=input()
y= map(int,raw_input().split())
t=input()

i=0
last=0

for v in range(0,t):
    p=input()
    last=0
    for i in range(0,len(y)):
        if(p<=(y[i]+last)):
            print i+1
            break;
        last=last+y[i]


