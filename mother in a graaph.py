class Graph:
    def __init__(self,data):
        self.vertice=data
        self.connections={}

    def add_edge(self,u,v):
        try:
            self.connections[u].append(v)
        except:
            self.connections[u]=[v]


    def dfs(self,i,visited):

        visited[i] = 1

        try:
            for j in self.connections[i]:
                if visited[j] ==0:
                    self.dfs(j,visited)
                else:
                    pass
        except:
            pass


    def print_mother(self):

        visited = [0] * self.vertice
        Contender_mother=-1

        for i in range(0,self.vertice):

            if visited[i] == 0:
                self.dfs(i,visited)
                Contender_mother=i

        visited=[0]*self.vertice
        self.dfs(Contender_mother,visited)

        for i in visited:
            if i==0:
                print "No"
                return

        print "yes and node is " ,Contender_mother


G=Graph(7)
G.add_edge(0,1)
G.add_edge(0,2)
G.add_edge(1,3)
G.add_edge(5,6)
G.add_edge(5,2)
G.add_edge(4,1)
G.add_edge(6,4)
G.add_edge(6,0)

G.print_mother()