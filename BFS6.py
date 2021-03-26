 from collections import defaultdict

class Graph:
   def __init__(self,V):
       self.vertex=V
       self.graph=defaultdict(list)
   def add_edges(self,u,v):
       self.graph[u].append(v)
   def BFS(self,u,k):
      visited=[False]*self.vertex
      queue=[]
      count=1
      queue.append(u)
      visited[u]=True
      while queue:
         q_length=len(queue)
         if k==1:
            print(queue)
            break
         while q_length:
            m=queue.pop(0)
            for i in self.graph[m]:
               if not visited[i]:
                 visited[i]=True
                 queue.append(i)
            q_length=q_length-1
         count=count+1
         if count==k:
             print(queue)

if __name__=="__main__":
   graph=Graph(4)
   graph.add_edges(2,0)
   graph.add_edges(0,2)
   graph.add_edges(1,2)
   graph.add_edges(0,1)
   graph.add_edges(2,3)
   graph.add_edges(3,3)
   graph.BFS(2,3)
   


         