import sys
from collections import deque
input=sys.stdin.readline
n=int(input())
graph=[list(input().rstrip()) for _ in range(n)]
graphRG=[[]for _ in range(n)]

for i in range(n):
  for j in range(n):
    if graph[i][j]=="G":
      graphRG[i].append("R")
    else:
      graphRG[i].append(graph[i][j])

  
def BFS(graph1):
  visited=[[0]*n for _ in range(n)]
  dx=[0,1,0,-1]
  dy=[-1,0,1,0]
  section=0
  for i in range(n):
    for j in range(n):
      
      if not visited[i][j]:
        visited[i][j]=1
        queue=deque()
        queue.append((i,j))
        while queue:
          y,x=queue.popleft()
          for k in range(4):
            cur_y=y+dy[k]
            cur_x=x+dx[k]
            if 0<=cur_x<n and 0<=cur_y<n:
              if not visited[cur_y][cur_x] and graph1[cur_y][cur_x]==graph1[y][x]:
                visited[cur_y][cur_x]=1
                queue.append((cur_y,cur_x))
        section+=1
       
  return section  

a=BFS(graph)
b=BFS(graphRG)
print(a,b)