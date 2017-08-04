x=input()
c=pow(2,x)-1
W=[]
L=[]
for i in range(0,c):
    y=map(str,raw_input().split())
    w=y[0]
    l=y[1]
    if(W.__contains__(w)==0):
         W.append(w)
    if(L.__contains__(l)==0  ):
        L.append(l)
C=[]
for x in set(W).intersection(L):
    W.remove(x)



print W[0]