
z=map(int,raw_input().split())
n=z[0]
c=z[1]
A={}
for i in range(0,n-1):
    k=map(str,raw_input().split())
    one=k[0]
    two=k[1]
    try:
        if(A[one]):
            A[one].append(two)


    except:
        A[one]=two

print A.items()

