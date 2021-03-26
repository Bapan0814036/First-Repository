class Cell:
   def __init__(self,x,y,dist):
       self.x=x
       self.y=y
       self.dest=dist

def is_inside(a,b,N,M):
   if a<0 or a>=N:
       return False
   if b<0 or b>=N:
       return False
   if M[a][b]==0:
       return False
   return True

def BFS(kpos,tpos,N,M):
   dx=[1,-1,0,0]
   dy=[0,0,1,-1]
   queue=[]
   queue.append(Cell(kpos[0],kpos[1],0))
   visited=[[0 for i in range(N)] for i in range(N)]
   visited[kpos[0]][kpos[1]]=True
   while queue:
      m=queue.pop(0)
      if m.x==tpos[0] and m.y==tpos[1]:
         return m.dest
      for i in range(4):
         x=m.x+dx[i]
         y=m.y+dy[i]
         if is_inside(x,y,N,M) and M[x][y]!='#':
            if visited[x][y]==0:
               queue.append(Cell(x,y,m.dest+1))
               visited[x][y]=1
   return -1

if __name__=="__main__":
   M=[[3,3,1,0],[3,0,3,3],[2,3,0,3],[0,3,3,3]]
   kpos=[0,2]
   tpos=[2,0]
   print(f"The minimum steps required is {BFS(kpos,tpos,4,M)}")
    
   