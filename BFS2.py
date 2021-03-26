def BFS(adj,u):
   queue=[]
   visited=[False]*vertex
   queue.append(u)
   visited[u]=True
   while queue:
       m=queue.pop(0)
       print(m)
       for i in adj[m]:
         if not visited[i]:
            visited[i]=True
            queue.append(i)
   
def create_adjacency_list(adj,u,v):
    adj[u].append(v)

if __name__=="__main__":
   vertex=int(input("Enter the no of vertices"))
   adj=[[] for i in range(vertex)]
   create_adjacency_list(adj,0,2)
   create_adjacency_list(adj,2,0)
   create_adjacency_list(adj,1,2)
   create_adjacency_list(adj,0,1)
   create_adjacency_list(adj,2,3)
   create_adjacency_list(adj,3,3)
   BFS(adj,2)

   
   
   
   