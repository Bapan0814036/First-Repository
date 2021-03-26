class Cell:
   def __init__(self,x,dist):
       self.x=x
       self.dest=dist


def is_inside(a,N):
   if a<0 or a>=N:
      return False
   return True

def BFS(l,x):
   dx=[-1,1]
   queue=[]
   visited=[False]*len(l)
   queue.append(Cell(x,0))
   visited[x]=True
   while queue:
      m=queue.pop(0)
      if m.x==(len(l)-1):
         return m.dest
      for i in range(2):
         k=m.x+dx[i]
         if is_inside(k,len(l)) and visited[k]==False:
               queue.append(Cell(k,m.dest+1))
               visited[k]=True
      indexes=[i for i,j in enumerate(l) if j==l[m.x]]
      indexes.remove(m.x)
      if indexes:
        for i in indexes:
            if visited[i]==False:
              queue.append(Cell(i,m.dest+1))
              visited[i]=True
   return -1

if __name__=="__main__":
   l=[0,1,2,3,4,5,6,7,5,4,3,6,0,1,2,3,4,5,7]
   N=len(l)
   print(BFS(l,0))

      
   
      