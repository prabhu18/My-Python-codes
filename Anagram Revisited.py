__author__ = 'pjha'

#a=['c','d']
#b=['d','c']

#print len(list(set(a) - set(b)))

x=input()
A=[]
B=[0]*x
for i in range(0,x):
    A.append(raw_input())

for j in range(0,x):
    for k in range(0,x):
        if(j==k):
            pass
        else:
            if(len(A[j])==len(A[k])):
                if( len(list(set(list(A[j]))-set(list(A[k]))))==0):
                    B[j]=B[j]+1
print max(B)+1




