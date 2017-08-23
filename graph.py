class graph:
    def __init__(self):
        self.graph_list={}


def add_Edge(g,u,v):
    try:
        g[u].append(v)
    except:
        g[u]=[v]

def print_all_node(gr,visited,v):
    visited[v]=True
    print v
    for i in gr[v]:
        try:
            if visited[i]==False:
                print_all_node(gr,visited,i)
        except:
            pass



def print_graph(gr):
    visited=[0]*6
    for i in range(0,6):
        if visited[i]==False:
            print_all_node(gr,visited,i)

gra=graph()
add_Edge(gra.graph_list,0,2)
add_Edge(gra.graph_list,1,3)
add_Edge(gra.graph_list,3,5)
add_Edge(gra.graph_list,2,4)
print_graph(gra.graph_list)
