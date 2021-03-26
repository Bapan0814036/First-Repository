class Cell:
   def __init__(self,x,dist):
      self.x=x
      self.dist=dist

def is_inside(a,N):
   if a<0 or a>=N:
       return False
   return True

def BFS(l,x):
   dx=[1,-1]
   visited=[False]*len(l)
   queue=[]
   queue.append(Cell(0,0))
   visited[x]=True
   while queue:
     m=queue.pop(0)
     if m.x==(len(l)-1):
        return m.dist
     for i in range(2):
        k=m.x+dx[i]
        if visited[k]==False and is_inside(k,len(l)):
           queue.append(Cell(k,m.dist+1))
           visited[k]=True
     new_list=[i for i,j in enumerate(l) if j==l[m.x]]
     new_list.remove(m.x)
     if new_list:
        for i in new_list:
          if not visited[i]:
             queue.append(Cell(i,m.dist+1))
             visited[i]=True
   return -1

if __name__=="__main__":
   l=[0, 1, 2, 3, 4, 5, 6, 7, 5, 4, 3, 6, 0, 1, 2, 3, 4, 5, 7]
   print(BFS(l,0))

   