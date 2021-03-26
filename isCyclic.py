#isCyclic

from collections import defaultdict

class Graph:

   def __init__(self,V):
       self.graph=defaultdict(list)
       self.vertex=V

   def add_edges(self,u,v):
       self.graph[u].append(v)

   def DFS(self):
      visited=[False]*self.vertex
      recstack=[False]*self.vertex
      for i in range(self.vertex):
         if not visited[i]:
            if self.DFS_util(visited,recstack,i):
                 return True
      return False


   def DFS_util(self,visited,recstack,u):
      visited[u]=True
      recstack[u]=True
      for i in self.graph[u]:
        if not visited[i]:
           if self.DFS_util(visited,recstack,i):
              return True
           elif i in recstack:
              return True
      recstack[u]=False
      return False

if __name__=="__main__":
   graph=Graph(4)
   graph.add_edges(2,0)
   graph.add_edges(0,2)
   graph.add_edges(1,2)
   graph.add_edges(0,1)
   graph.add_edges(2,3)
   graph.add_edges(3,3)
   print(graph.DFS())


