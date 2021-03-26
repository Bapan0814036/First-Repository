class Cell:
   def __init__(self,x,y,dist):
      self.x=x
      self.y=y
      self.dest=dist

def is_inside(a,b,N):
    if a<0 or a>=N:
      return False
    if b<0 or b>=N:
      return False
    return True

def BFS(kpos,tpos,N):
   dx=[2,2,-2,-2,1,-1,1,-1]
   dy=[1,-1,1,-1,2,2,-2,-2]
   queue=[]
   queue.append(Cell(kpos[0],kpos[1],0))
   visited=[[False for i in range(N)] for i in range(N)]
   visited[kpos[0]][kpos[1]]=True
   while queue:
      m=queue.pop(0)
      if m.x==tpos[0] and m.y==tpos[1]:
         return m.dest
      for i in range(8):
        x=m.x+dx[i]
        y=m.y+dy[i]
        if visited[x][y]==False and is_inside(x,y,N):
           queue.append(Cell(x,y,m.dest+1))
           visited[x][y]=True
   return -1

if __name__=="__main__":
   kpos=[2,3]
   tpos=[4,5]
   print(BFS(kpos,tpos,6))

   

   
   