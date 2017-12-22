import heapq

s='ABCDBAGHCHFAC'
K=3
D={}
for i in range(0,len(s)):
    try:
        D[s[i]][0]=D[s[i]][0]+1
        D[s[i]][1]=i
    except:
        D[s[i]]=[1,i]
heap=[]

for i in D.values():
    if i[0]==1:
        heapq.heappush(heap,i[1])

for j in range(0,K):
    print s[heapq.heappop(heap)],
