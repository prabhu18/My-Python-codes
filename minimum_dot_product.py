# Uses python2
__author__ = 'pjha'

import sys

def min_dot_product(a, b):

    res = 0
    max_a = 0
    min_b = 0
    while(b.__len__()>0):
        max_a=max(a)
        min_b=min(b)
        res=res+max_a*min_b
        a.remove(max_a)
        b.remove(min_b)

    return res

if __name__ == '__main__':
    x=input()
    a=map(int,raw_input().split())
    b=map(int,raw_input().split())
    print(min_dot_product(a, b))
