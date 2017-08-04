__author__ = 'pjha'
def bitsoncount(x):
    return bin(x).count('1')
x=input()
for i in range(0,x):
    z=map(int,raw_input().split())
    n=z[0]
    c=z[1]
    A=[]
    array=map(int,raw_input().split())
    for j in array:
        A.append(bitsoncount(j))
    p=0
    sum=0
    A.sort(reverse=True)
    while(p<c):
        sum=sum+A[p]
        p=p+1
    print sum