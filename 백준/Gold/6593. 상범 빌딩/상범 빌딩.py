import sys
input=sys.stdin.readline
from collections import deque
dz=[0,0,1,-1,0,0]
dy=[0,0,0,0,-1,1]
dx=[1,-1,0,0,0,0]
def BFS(arr,visited,z,y,x):
  visited[z][y][x]=1
  L=len(visited)
  R=len(visited[0])
  C=len(visited[0][0])
  queue=deque()
  queue.append([z,y,x])
  
  while queue:
    
    z1,y1,x1=queue.popleft()
    
    for i in range(6):
      cur_z=z1+dz[i]
      cur_y=y1+dy[i]
      cur_x=x1+dx[i]
      
      if 0<=cur_z<L and 0<=cur_y<R and 0<=cur_x<C:
        if arr[cur_z][cur_y][cur_x]=='E':
          cnt=visited[z1][y1][x1]
          return f'Escaped in {cnt} minute(s).'
        if arr[cur_z][cur_y][cur_x]=='.' and not visited[cur_z][cur_y][cur_x]:
          visited[cur_z][cur_y][cur_x]=visited[z1][y1][x1]+1
          queue.append([cur_z,cur_y,cur_x])
    
  return 'Trapped!'        
    
  

while True:
  L,R,C=map(int,input().split())
  if L==0 and R==0 and C==0:
    break
  buildings=[[] for _ in range(L)]
  visited=[[[0]*C for j in range(R)] for i in range(L)]
  for i in range(L):
    for j in range(R):
      buildings[i].append(list(input().rstrip('\n')))
    input()
  for z in range(L):
    for y in range(R):
      for x in range(C):
        if buildings[z][y][x]=='S':
          print(BFS(buildings,visited,z,y,x))