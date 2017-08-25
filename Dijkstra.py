class Graph:
    def __init__(self,V):
        self.vertices=V
        self.graph=[[0 for x in range (0,V) ] for x in range  (0,V)]

def min_distance(distance,C,vertices_include):
    min= 999999

    for i in range(0,C):
        if distance[i]<min and vertices_include[i]==0:
            min=distance[i]
            min_index=i
    return min_index

def print_solution(distance,C):
    for i in range(0,C):
        print 'node: ',i, ' and its distance :' , distance[i]

def Disjkstra(graph,src,C):
    distance=[999999]*C
    vertices_include=[0]*C
    distance[src]=0

    for i in range(0,C):

        u=min_distance(distance,C,vertices_include)

        vertices_include[u]=1
        for j in range(0,C):
            if graph[u][j]>0 and vertices_include[j]==0 and distance[j]>(distance[u]+graph[u][j]):
                distance[j]=distance[u]+graph[u][j]


    print_solution(distance,C)

g=Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]]
Disjkstra(g.graph,0,g.vertices)