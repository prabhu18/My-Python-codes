__author__ = 'pjha'
for i in range(0,input()):
    y=0
    x=input()
    if(x%8==0 and y==0):
        print 'Side Upper'
        y=1

    if(x in(7,15,23,31,39,47,55,63,71) and y==0):
        print 'Side Lower'
        y=1
    if(x in (1, 4, 9, 12, 17, 20, 25 ,28, 33, 36, 41, 44, 49, 52, 57, 60, 65, 68)and y==0):
        print 'Lower'
        y=1
    if(x in (3,6,11,14,19,22,27,30,35,38,43,46,51,54,59,62,67,70)and y==0):
        print 'Upper'
        y=1
    if(y==0):
        print 'Middle'
        y=1



