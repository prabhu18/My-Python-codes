from collections import defaultdict
import sys

def get_node_val(visited,node_val,d,source):

    queue=[]
    queue.append(source)
    total_count=0

    while(len(queue)!=0):
        temp=queue.pop(0)
        visited[temp]=1
        total_count=total_count+node_val[temp]
        for neighbor in d[temp]:

            if visited[neighbor]!= 1:
                queue.append(neighbor)

    print total_count
d=defaultdict(list)
node_val=defaultdict(int)
visited=defaultdict(int)
val=[[1, 5, [3]], [2, 3, [1]], [3, 3, []]]
source=2
for i in val:
    d[i[0]]=i[2]
    node_val[i[0]]=i[1]
get_node_val(visited,node_val,d,source)

