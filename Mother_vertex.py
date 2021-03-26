from collections import defaultdict
#Mother Vertex

class Graph:

    def __init__(self,V):
       self.graph=defaultdict(list)
       self.vertex=V

    def add_edges(self,u,v):
       self.graph[u].append(v)

    def DFS_util(self,visited,u):
        visited[u]=True
        for i in self.graph[u]:
           if not visited[i]:
               self.DFS_util(visited,i)
    
    def find_mother_vertex(self):
        visited=[False]*self.vertex
        v=0
        for i in range(self.vertex):
           if not visited[i]:
              self.DFS_util(visited,i)
              v=i
        visited=[False]*self.vertex
        self.DFS_util(visited,i)
        if False not in visited:
           print("There is no mother vertex")
        else:
           print(f"Mother vertex is {v}")

if __name__=="__main__":
   graph=Graph(4)
   graph.add_edges(2,0)
   graph.add_edges(0,2)
   graph.add_edges(1,2)
   graph.add_edges(0,1)
   graph.add_edges(2,3)
   graph.add_edges(3,3)
   graph.find_mother_vertex()



              