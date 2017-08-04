#!/bin/python

import sys

def birthdayCakeCandles(n, ar):
    ar.sort(reverse=True)
    cnt,i=0,0
    z=ar[i]


    while(i<len(ar) and ar[i]==z ):
        cnt=cnt+1
        i=i+1
        
    return cnt



n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = birthdayCakeCandles(n, ar)
print(result)
