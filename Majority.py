# Uses python2
__author__ = 'pjha'

import sys

def get_majority_element(a):
    maj=0
    count=1
    for i in range(1,a.__len__()):
        if(a[maj]==a[i]):
            count = count+1
        else:
            count= count-1

        if(count==0):
            maj=i
            count=1
    return a[maj]



if __name__ == '__main__':
    n=input()
    x=map(int,raw_input().split())
    if x.count(get_majority_element(x))>x.__len__()/2:
        print(1)
    else:
        print(0)
