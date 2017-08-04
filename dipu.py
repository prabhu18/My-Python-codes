def divisors(n):
    count=2 # accounts for 'n' and '1'
    i=2
    if(n==1):
        return  1
    while(i**2 <= n):
        if(n%i==0 and i**2==n):
            count+=1
        if(n%i==0 and i**2!=n):
            count+=2
        i+=1
    return count

print divisors(6)

