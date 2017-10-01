#!/bin/python

import sys

def issafe(x,y,n,d):
    if x>=0 and x< n and y>=0 and y<n:
        try:
            key=str(x)+'|'+str(y)
            if d[key]:
                return False
        except:
            return True
    else:
        return False

n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
d={}
rQueen,cQueen = raw_input().strip().split(' ')
rQueen,cQueen = [int(rQueen),int(cQueen)]

d={}
for a0 in xrange(k):
    rObstacle,cObstacle = raw_input().strip().split(' ')
    rObstacle,cObstacle = [int(rObstacle),int(cObstacle)]
    key=str(rObstacle-1)+'|'+str(cObstacle-1)
    d[key]=True

x=rQueen-1
y=cQueen-1
count=0

while( issafe(x,y,n,d) ):
    count=count+1
    x=x-1
    y=y-1


x=rQueen-1
y=cQueen-1

while( issafe(x,y,n,d) ):
    count=count+1
    x=x+1
    y=y+1


x=rQueen-1
y=cQueen-1

while( issafe(x,y,n,d) ):
    count=count+1
    y=y-1


x=rQueen-1
y=cQueen-1

while( issafe(x,y,n,d) ):
    count=count+1
    y=y-1
    x=x+1


x=rQueen-1
y=cQueen-1


while( issafe(x,y,n,d) ):
    count=count+1
    y=y+1
    x=x-1


x=rQueen-1
y=cQueen-1

while( issafe(x,y,n,d) ):
    count=count+1
    x=x+1


x=rQueen-1
y=cQueen-1

while( issafe(x,y,n,d) ):
    count=count+1
    x=x-1

x=rQueen-1
y=cQueen-1

while( issafe(x,y,n,d) ):
    count=count+1
    y=y+1


print count-8
