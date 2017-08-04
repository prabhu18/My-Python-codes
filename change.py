# Uses python2
__author__ = 'pjha'

import sys

def get_change(n):
    c=0
    a=[10,5,1]
    while(n>0):
        k=max(a)
        if(k>n):
            a.remove(k)
        else:
            c=c+n/k
            n=n%k


    return c

if __name__ == '__main__':
    n = input()
    print(get_change(n))
