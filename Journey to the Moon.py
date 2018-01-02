import math
from collections import defaultdict
def journeyToMoon(node,d,visited,count):
    visited[node]=1
    count.append(node)

    for i in d[node]:
        if visited[i]==0:
            journeyToMoon(i,d,visited,count)


n, p = raw_input().strip().split(' ')
n, p = [int(n), int(p)]
astronaut = []
result=1
for astronaut_i in xrange(p):
    astronaut_temp = map(int, raw_input().strip().split(' '))
    astronaut.append(astronaut_temp)
visited = [0] * n

d = defaultdict(list)

for i in astronaut:
    d[i[0]].append(i[1])
    d[i[1]].append(i[0])


def nCr(n,r):
    f = math.factorial
    if r>n:
        return 0
    return f(n) / f(r) / f(n-r)

total=nCr(n,2)

"""
#for DFS Approach, Might touch maximum depth error

for i in range(0,n):
    if visited[i]==0:
        count=[]
        journeyToMoon(i,d,visited,count)
        print count
        total=total-nCr(len(count),2)
"""

#for BFS Approach,
for i in range(0,n):
    stack=[]
    count=0
    if visited[i]==0:
        stack.append(i)
        visited[i]=1
        while len(stack)>0:
            temp=stack.pop()
            count=count+1
            for j in d[temp]:
                if visited[j]==0:
                    stack.append(j)
                    visited[j]=1

        total = total - nCr(count, 2)

print total