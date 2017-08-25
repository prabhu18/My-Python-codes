class graph:
    def __init__(self,V):
        self.vertices=V
        self.node={}



def addedge(g,u,v):
    try:
        g[u].append(v)
    except:
        g[u]=[v]

def find_parent(parent,i):
    if parent[i]==-1:
        return i
    else:
        return find_parent(parent,parent[i])

def union(parent,x,y):
    x=find_parent(parent,x)
    y=find_parent(parent,y)

    parent[x]=y

def detect_cycle(node,V):
    parent=[-1]*V

    for i in range(0,V):
        try:
            for j in node[i]:
                x=find_parent(parent,i)
                y=find_parent(parent,j)
                if x==y:
                    return True
                else:
                    union(parent,i,j)
        except:
            pass

    return False

directed_graph=graph(4)
addedge(directed_graph.node,0,1)
addedge(directed_graph.node,2,0)
addedge(directed_graph.node,1,2)

if detect_cycle(directed_graph.node,directed_graph.vertices) is True:
    print 'Cycle'
else:
    print 'No Cycle'
