__author__ = 'pjha'



def max_ht(x,y):
    x.sort()
    return x[y-1]+x[y-2]+1

x=map(int,raw_input().split())
y=input()

print max_ht(x,y)
