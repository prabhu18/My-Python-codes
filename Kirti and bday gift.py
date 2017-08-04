x=input()
A=[]
for i in range(0,x):
    A.append(raw_input())

y=input()
for j in range(0,y):
    c=map(str,raw_input().split())
    L=int(c[0])
    R=int(c[1])
    S=c[2]
    count=0
    print A[L-1:R].count(S)