def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n /= 10
    return s

def is_prime(n):
    if(n<=3):
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True




for i in range(0,input()):
    x=input()
    y=sum_digits(x)
    if( is_prime(y)):
        print 'YES'
    else:
        print 'NO'