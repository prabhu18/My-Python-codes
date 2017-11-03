import sys
N = input()
K = input()
x = [input() for _ in range(0,N)]
x.sort()

i=0
j=K-1
diff=sys.maxint

min=x[i]
max=x[j]


while(i<=N-K+1 and j<N):

    temp=x[j]-x[i]
    if diff>temp:
        diff=temp
    i=i+1
    j=j+1

print diff
