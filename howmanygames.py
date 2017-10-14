#!/bin/python

import sys


def howManyGames(a, b, c, s):
    if s - a < 0:
        return 0
    s = s - a
    count = 1

    while (a > c):
        a = a - b
        s = s - a
        count = count + 1
        if s < 0:
            return count - 1

    s = s + a
    count = count - 1
    while (s >= c):
        s = s - c
        count = count + 1
    return count


if __name__ == "__main__":
    p, d, m, s = raw_input().strip().split(' ')
    p, d, m, s = [int(p), int(d), int(m), int(s)]
    answer = howManyGames(p, d, m, s)
    print answer
