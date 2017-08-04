def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n /= 10
    return s

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


x=input()
for i in range(0,x):
    y=input()
    if(is_prime(sum_digits(y)) and is_prime(y)):
        print 'YES'
    else:
        print 'NO'