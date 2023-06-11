import sys
input=sys.stdin.readline
from collections import deque
m,n,k=map(int,input().split())
graph=[[1]*n for _ in range(m)]
for i in range(k):
  x1,y1,x2,y2=map(int,input().split())
  for j in range(y1,y2):
    for t in range(x1,x2):
      graph[m-1-j][t]=0
 
visited=[[0]*n for _ in range(m)]
area=[]

def BFS(i,j):
  dy=[-1,0,1,0]
  dx=[0,1,0,-1]
  queue=deque()
  queue.append([i,j])
  cnt=1
  while queue:
    y,x=queue.popleft()
    for k in range(4):
      cur_y=y+dy[k]
      cur_x=x+dx[k]
      if 0<=cur_x<n and 0<=cur_y<m:
        if graph[cur_y][cur_x]==1 and not visited[cur_y][cur_x]:
          visited[cur_y][cur_x]=1
          queue.append([cur_y,cur_x])
          cnt+=1
  return cnt
 

for i in range(m):
  for j in range(n):
    if graph[i][j]==1 and not visited[i][j]:
      visited[i][j]=1
      area.append(BFS(i,j))
print(len(area))
area.sort()

print(' '.join(list(map(str,area))))