
from __future__ import division
for i in range(0,input()):
    l=input()
    y=sum(map(int,raw_input().split()))

    sum1=y/(l*100)

    sum1=sum1*100

    print round(sum1, 8)