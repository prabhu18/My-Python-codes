x=input()
y= map(int,raw_input().split())
t=input()

M = [[] for j in range(x)]

i=0
last=0
for k in y:

    if(i==0):
        while(k>0):
            M[i].append(k)
            k=k-1
        i=i+1


    else:
        last = len(M[i-1])
        while(k>0):
            M[i].append(k+last)
            k=k-1
        i=i+1

for y in range(0,t):
    p=input()
    i=0
    for list in M:
        if(list.__contains__(p)):
            print i+1
        else:
            i=i+1


