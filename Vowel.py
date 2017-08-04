x=input()
for i in range(0,x):
    z=raw_input()
    A=list(z)
    i=0
    while(i<len(A)):
        i=i+1
        for k in A:
            if(k not in ('a','e','i','o','u') or k not in ('A','E','I','O','U')):
                A.remove(k)

    print ''.join(A)