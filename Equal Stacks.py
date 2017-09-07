#!/bin/python

import sys


def get_largest(sum1, sum2, sum3):
    if sum1 > sum2:
        if sum3 < sum1:
            return 1
        else:
            return 3
    else:
        if sum2 < sum3:
            return 3
        else:
            return 2


n1, n2, n3 = raw_input().strip().split(' ')
n1, n2, n3 = [int(n1), int(n2), int(n3)]
h1 = map(int, raw_input().strip().split(' '))
h2 = map(int, raw_input().strip().split(' '))
h3 = map(int, raw_input().strip().split(' '))
flag = 1

while ((sum(h1) == sum(h2) == sum(h3)) is False):

    a = sum(h1)
    b = sum(h2)
    c = sum(h3)

    if a == 0 or b == 0 or c == 0:
        print 0
        flag = 0
        break

    largest = get_largest(a, b, c)

    if largest == 1:
        h1.pop(0)

    if largest == 2:
        h2.pop(0)

    if largest == 3:
        h3.pop(0)

if flag == 1:
    print sum(h1)


