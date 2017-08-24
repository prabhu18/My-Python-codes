class graph:
    def __init__(self,V):
        self.vertices=V
        self.node={}



def addedge(g,u,v):
    try:
        g[u].append(v)
    except:
        g[u]=[v]



def check_cycle(node,V,i,stack,visited):
    stack[i]=1
    visited[i]=1

    try:
        for j in node[i]:

            if visited[j]==0:
                if check_cycle(node,V,j,stack,visited)==1:
                    return True
            else:
                if stack[j]==1:
                    return True
    except:
        pass

    stack[i]=0
    return False


def is_cyclic(node,V):
    visited=[0]*V
    stack=[0]*V


    for i in range(0,V):
        if visited[i]==0:
            if check_cycle(node,V,i,stack,visited)==True:
                return True

    return False

directed_graph=graph(4)
addedge(directed_graph.node,0,1)
addedge(directed_graph.node,0,2)
addedge(directed_graph.node,1,2)
addedge(directed_graph.node,2,0)
addedge(directed_graph.node,2,3)
addedge(directed_graph.node,3,3)

if is_cyclic(directed_graph.node,directed_graph.vertices) ==1 :
    print 'Graph is cyclic'
else:
    print 'Graph is acyclic'