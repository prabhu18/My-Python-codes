
# Uses python2
__author__ = 'pjha'
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here

    return value


if __name__ == "__main__":
    data = map(int,raw_input().split())
    n, capacity = data[0:2]
    for i in range(0,n):

    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
