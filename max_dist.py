__author__ = 'pjha'


def truncate(f, n):
    s = '{}'.format(f)
    if 'e' in s or 'E' in s:
        return '{0:.{1}f}'.format(f, n)
    i, p, d = s.partition('.')
    return '.'.join([i, (d+'0'*n)[:n]])

l=input()
x=map(float,raw_input().split())
y=map(float,raw_input().split())
f=float(input())
z=[]

for i in range(0,len(x)):
    z.append(y[i]/x[i])
print truncate((f/min(z)),3)


