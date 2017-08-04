'''
# Read input from stdin and provide input before running code

name = raw_input('What is your name?\n')
print 'Hi, %s.' % name
'''
#print 'Hello World!'
t=int(raw_input())

for i in range(t):
    N,M=map(int,raw_input().split())
    t=float('inf')
    print t
    f=[t for i in range(N)]
    print f
    f[0]=0
    vs=[0]
    o1=[0]*N
    o1[0]=1
    l=[[] for j in range(N)]
    for j in range(M):
        x,y=map(int, raw_input().split())
        l[x-1].append(y-1)
        l[y-1].append(x-1)
        if(x==1):
            f[y-1]=1
            vs.append(y-1)
        if(y==1):
            f[x-1]=1
            vs.append(x-1)
    print l
    while(len(vs)<N):
        for o in vs:
            if(o1[o]==1):
                continue
            for p in l[o]:
                if f[p]>f[o]:
                    f[p]=f[o]+1
                    vs.append(p)
            o1[o]=1
    print vs
    print(f[-1])