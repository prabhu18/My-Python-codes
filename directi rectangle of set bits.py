
__author__ = 'pjha'


from collections import namedtuple
from operator import mul
Info = namedtuple('Info', 'start height')
def max_size(mat, value):
    it = iter(mat)
    hist = [(el==value) for el in next(it, [])]
    max_size = max_rectangle_size(hist)
    for row in it:
        hist = [(1+h) if el == value else 0 for h, el in zip(hist, row)]
        max_size = max(max_size, max_rectangle_size(hist), key=area)
    return max_size

def max_rectangle_size(histogram):
    stack = []
    top = lambda: stack[-1]
    max_size = (0, 0)
    pos = 0
    for pos, height in enumerate(histogram):
        start = pos
        while True:
            if not stack or height > top().height:
                stack.append(Info(start, height))
            elif stack and height < top().height:
                max_size = max(max_size, (top().height, (pos - top().start)),
                               key=area)
                start, _ = stack.pop()
                continue
            break

    pos += 1
    for start, height in stack:
        max_size = max(max_size, (height, (pos - start)), key=area)
    return max_size

def area(size):
    return reduce(mul, size)

for i in range(0,input()):
    a=map(int,raw_input().split())
    N=a[0]
    M=a[1]
    Array=[]
    for j in range(0,3):
        Array.append([0]*N)
    for k in range(0,M):
        b=map(int,raw_input().split())
        R=b[0]
        C1=b[1]
        C2=b[2]
        while(C1<=C2):
            Array[R-1][C1-1]=1
            C1=C1+1
    x=max_size(Array,1)
    print x[0]*x[1]




