from collections import  defaultdict

def dfs(vertice,visited,number_of_vertices,edges):

    visited[vertice]=1
    count=1
    for neighbor in edges[vertice]:
        if visited[neighbor]==0:
            count=count+dfs(neighbor,visited,number_of_vertices,edges)
    return count


queries=input()
for i in range(0,queries):

    info=map(int,raw_input().split(' '))
    number_of_vertices=info[0]
    number_of_edge=info[1]
    cost_lib=info[2]
    cost_road=info[3]
    edges=defaultdict(list)


    for j in range(0,number_of_edge):
        road=map(int,raw_input().split(' '))
        a=road[0]-1
        b=road[1]-1

        edges[a].append(b)
        edges[b].append(a)

    if cost_road >= cost_lib:
        print cost_lib * number_of_vertices
    else:

        disconnected_graph=0
        visited=[0]*number_of_vertices
        cost=0

        for k in range(0,number_of_vertices):

            if visited[k]==0:
                count=dfs(k,visited,number_of_vertices,edges)
                disconnected_graph=disconnected_graph+1
                if count>1:
                    cost=cost+(count-1)*cost_road


        print disconnected_graph*cost_lib+cost

