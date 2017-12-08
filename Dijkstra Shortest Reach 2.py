import sys

def get_minimum_index(visited,distance,number_of_vertices):
    min=sys.maxint

    for i in range(0,number_of_vertices):
        if min>=distance[i] and visited[i] ==0:
            min=distance[i]
            index=i

    return index


def get_minimum_path_from_vertex(visited,distance,graph_matrix,source,number_of_vertices):


    for i in range(0,number_of_vertices):
        u = get_minimum_index(visited, distance, number_of_vertices)
        visited[u]=1

        for j in range(0,number_of_vertices):

            if graph_matrix[u][j] !=0 and visited[j] ==0 and distance[u] != sys.maxint and graph_matrix[u][j]+distance[u]<=distance[j]:
                distance[j]=graph_matrix[u][j]+distance[u]

    for j in range(0,number_of_vertices):
        if j==source:
            pass
        else:
            if distance[j]==sys.maxint:
                print -1,
            else:
                print distance[j],
    print



for i in range(0,input()):
    val=map(int,raw_input().split(' '))
    number_of_vertices=val[0]
    number_of_edges=val[1]
    graph_matrix=[[0 for i in range(number_of_vertices)] for j in range(number_of_vertices)]
    for k in range(number_of_edges):
        val2=map(int,raw_input().split(' '))
        parent=val2[0]
        child=val2[1]
        edge_value=val2[2]
        if graph_matrix[parent-1][child-1] != 0:
            if graph_matrix[parent-1][child-1]>edge_value:
                graph_matrix[parent - 1][child - 1]=edge_value
                graph_matrix[child - 1][parent - 1] = edge_value
        else:
            graph_matrix[parent - 1][child - 1] = edge_value
            graph_matrix[child - 1][parent - 1] = edge_value

    source=input()-1

    visited=[0]*number_of_vertices
    distance=[sys.maxint]*number_of_vertices
    distance[source]=0

    get_minimum_path_from_vertex(visited,distance,graph_matrix,source,number_of_vertices)


