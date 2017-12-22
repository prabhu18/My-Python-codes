import heapq
a="tree"
d = {}

for i in range(0, len(a)):
    try:
        d[a[i]][0] = d[a[i]][0] + 1
    except:
        d[a[i]] = [1, i]

heap = []
for j in d.values():
    j[0] = -j[0]
    heapq.heappush(heap, j)
r = []
while(len(heap)>0):
    temp = heapq.heappop(heap)
    count=-temp[0]
    while(count>0):
        r.append(a[temp[1]])
        count=count-1
print ''.join(r)