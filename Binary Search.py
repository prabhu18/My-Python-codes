# Uses python2
__author__ = 'pjha'

import sys

def binary_search(arr,num):
    f=0
    l=len(arr)-1
    found=0
    r=-1
    found=False
    while(f<=l and found == False):
        m=(f+l)/2

        if(num==arr[m]):
            found=True
            r=m
        else:
            if(num>arr[m]):
                f=m+1
            else:
                l=m-1
    return r



if __name__ == '__main__':
    x=map(int,raw_input().split())
    arr=x[1:]
    y=map(int,raw_input().split())
    sea=y[1:]
    z=[]
    for i in range(0,y[0]):
        print (binary_search(arr,sea[i])),



