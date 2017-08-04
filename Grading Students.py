#!/bin/python

import sys

def solve(grades):
    a=[]

    for i in range(0,len(grades)):
        if grades[i]<38:
            a.append(grades[i])
        else:
            mod=grades[i]%5
            div=grades[i]/5

            if (div+1)*5-grades[i]<3:
                a.append((div+1)*5)
            else:
                a.append(grades[i])

    return a


n = int(raw_input().strip())
grades = []
grades_i = 0
for grades_i in xrange(n):
    grades_t = int(raw_input().strip())
    grades.append(grades_t)
result = solve(grades)
print "\n".join(map(str, result))