
def check_prime(number):
    if number == 1:
        return False, 1
    elif number < 4:
        return True, number
    else:
        i = 0
        max_range = int(sqrt(number))+1
        for i in xrange(2, max_range):
            if number % i == 0:
                return False, i
        return True, i

if __name__ == '__main__':
    from math import sqrt
    for t in range(0,input()):
        count = 0
        test_prime = input()
        if check_prime(test_prime)[0]:
            count = 1
        else:
            count = 0
        for num in xrange(test_prime, 10**6, test_prime):
            result = check_prime(num)
            if result[1] == test_prime:
                count += 1

        print count
