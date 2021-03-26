class Graph:

   def __init__(self,V):
       self.vertex=V
       self.graph=[]

   def add_edges(self,u,v,w):
       self.graph.append([u,v,w])

   def display_dest(self,dest,src):
      for i in dest:
        print(f"({src},{dest.index(i)})----->{i}")

   def bellman_ford(self,src):
       dest=[float("Inf")]*self.vertex
       dest[src]=0
       for i in range(self.vertex-1):
          for u,v,w in self.graph:
            if dest[u]!=float("Inf") and dest[u]+w<dest[v]:
               dest[v]=dest[u]+w
       self.display_dest(dest,src)
       for i in range(self.vertex-1):
         for u,v,w in self.graph:
             if dest[u]+w<dest[v]:
                print(f"{v} is effected by cycle")


if __name__=="__main__":
   graph=Graph(5)
   graph.add_edges(0,1,-1)
   graph.add_edges(0,2,4)
   graph.add_edges(1,2,3)
   graph.add_edges(1,3,2)
   graph.add_edges(1,4,2)
   graph.add_edges(3,2,5)
   graph.add_edges(3,1,1)
   graph.add_edges(4,3,-3)
   graph.bellman_ford(0)
       
       
       
            
       