# Uses python2
x=input()
z=map(int,raw_input().split())

if(z[0]>=z[1]):
    max_1=z[0]
    max_2=z[1]
else:
    max_1=z[1]
    max_2=z[0]

for i in range(1,x):
    if(z[i]>max_1):
        max_2=max_1
        max_1=z[i]
    else:
        if(z[i]>=max_2 and i>=2 ):
            max_2=z[i]

print max_1*max_2