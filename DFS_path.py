from collections import defaultdict

class Graph:

   def __init__(self,V):
       self.graph=defaultdict(list)
       self.vertex=V

   def add_edges(self,u,v):
       self.graph[u].append(v)

   def find_path_util(self,visited,path,u,v):
       visited[u]=True
       path.append(u)
       if u==v:
          print(path)
       else:
         for i in self.graph[u]:
           if not visited[i]:
              self.find_path_util(visited,path,i,v)
       path.pop()
       visited[u]=False

   def find_path(self,u,v):
      visited=[False]*self.vertex
      path=[]
      self.find_path_util(visited,path,u,v)

if __name__=="__main__":
   graph=Graph(4)
   graph.add_edges(0,2)
   graph.add_edges(2,0)
   graph.add_edges(1,2)
   graph.add_edges(0,1)
   graph.add_edges(2,3)
   graph.add_edges(3,3)
   graph.add_edges(1,3)
   print("Printing all the path reachable from 2 to 3")
   graph.find_path(2,3)


