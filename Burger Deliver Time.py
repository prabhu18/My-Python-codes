import operator
x=input()
A={}
for i in range(1,x+1):
    y=map(int,raw_input().split())
    A[i]=y[0]+y[1]
sorted_x = sorted(A.items(), key=operator.itemgetter(1))
for x in sorted_x:
    print x[0],