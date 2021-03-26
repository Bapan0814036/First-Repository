from collections import defaultdict

class Graph:
   def __init__(self,V):
      self.graph=defaultdict(list)
      self.vertex=V
   def add_edges(self,u,v):
      self.graph[u].append(v)
      self.graph[v].append(u)

   def display(self):
      for i in self.graph:
        print(f"{i}--->{self.graph[i]}")

   def K_core(self,k):
      queue=[]
      while True:
         for i in self.graph:
            if len(self.graph[i])<k:
               queue.append(i)
         for i in queue:
            del self.graph[i]
         if queue:
            for i in self.graph:
               for j in self.graph[i]:
                  if j in queue:
                     self.graph[i].remove(j)
            queue[:]=[]
         else:
            break

if __name__=="__main__":
   k=9
   graph=Graph(9)
   graph.add_edges(0,1)
   graph.add_edges(0,2)
   graph.add_edges(1,2)
   graph.add_edges(1,5)
   graph.add_edges(2,3)
   graph.add_edges(2,4)
   graph.add_edges(2,5)
   graph.add_edges(2,6)
   graph.add_edges(3,4)
   graph.add_edges(3,6)
   graph.add_edges(3,7)
   graph.add_edges(4,6)
   graph.add_edges(4,7)
   graph.add_edges(5,6)
   graph.add_edges(5,8)
   graph.add_edges(6,7)
   graph.add_edges(6,8)
   graph.K_core(3)
   graph.display()

             