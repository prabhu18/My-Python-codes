from collections import defaultdict
import sys
def get_distance_nodes(source,target,number_of_nodes,d):
    distance=[sys.maxint]*number_of_nodes
    queue=[]
    distance[source-1]=0
    queue.append(source)
    counter=1
    while(len(queue)!=0):
        temp=queue.pop(0)

        for neighbor in d[temp]:
            if distance[neighbor-1]== sys.maxint:
                distance[neighbor-1]=counter
                queue.append(neighbor)
        counter=counter+1
    print distance

number_of_node=input()
number_of_edges=input()
d=defaultdict(list)
for i in range(0,number_of_edges):
    val=raw_input().split(' ')
    from_node=int(val[0])
    to_node=int(val[1])
    d[from_node].append(to_node)
    d[to_node].append(from_node)

source_node=input()
target_node=input()
get_distance_nodes(source_node,target_node,number_of_node,d)