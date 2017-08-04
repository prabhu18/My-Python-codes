def is_prime(n):
    A=[2,3]
    for num in range(3,n+1):
        prime = True
        for i in range(2,(n/2)+1):
            if (num%i==0):
                prime = False
        if prime:
            if A.__contains__(num)==False:

                A.append(num)
    print A
    return A

def fact(j):
    if j<=1:
        return  1
    else:
        return j*fact(j-1)

x=input()
for j in is_prime(x):
    print fact(j)