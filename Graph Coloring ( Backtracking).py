class Graph:
    def __init__(self,V):
        self.vertices=V
        self.graph=[[0 for x in range (0,V) ] for x in range  (0,V)]

def is_safe(graph,col,vertex,number_of_vertex,color):
    for i in range(0,number_of_vertex):
        if graph[vertex][i]==1 and color[i]==col:
            return False
    return True


def graph_color(graph,m,color,vertex,number_of_vertex):
    if vertex==number_of_vertex:
        return True

    for i in range(1,m+1):

        if is_safe(graph,i,vertex,number_of_vertex,color) is True:
            color[vertex] = i
            if graph_color(graph,m,color,vertex+1,number_of_vertex) is True:
                return True
            color[vertex]=0

    return False



G=Graph(4)
G.graph=[[0,1,1,1], [1,0,1,0], [1,1,0,1], [1,0,1,0]]
m=3
color=[0]*4
if graph_color(G.graph,m,color,0,G.vertices) is True:
    print 'Possible, Just assign these colors to corresponding index ' , color
else:
    print 'Not possible'