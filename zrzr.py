__author__ = 'pjha'

def trailing_zero(n):
    i=5
    count=0
    while(n/i>=1):
        count = count+n/i
        i=i*5

    return count

for i in range(0,input()):
    print trailing_zero(input())