import sys
from collections import deque
input=sys.stdin.readline
dx=[]
dy=[]
dv=[(0,-1),(1,0),(0,1),(-1,0)]
n,m=map(int,input().split())
r,c,d=map(int,input().split())
graph=[]

for i in range(n):
    graph.append(list(map(int,input().split())))

queue=deque()
queue.append((r,c,d))

cnt=1
while queue:
    
    y,x,direction=queue.popleft()
    graph[y][x]=2
    startd=direction
    for i in range(4):
        x1=x+dv[i][0]
        y1=y+dv[i][1]
        if 0<=x1 and x1<=m-1 and 0<=y1 and y1<=n-1 and graph[y1][x1]==0:
            direction=(direction-1)%4
            break
            
    if startd==direction:
        x1=x-dv[direction][0]
        y1=y-dv[direction][1]
        if 0<=x1 and x1<=m-1 and 0<=y1 and y1<=n-1 and graph[y1][x1]==2:
           queue.append((y1,x1,direction)) 
            

    else:
        x1=x+dv[direction][0]
        y1=y+dv[direction][1]
        if 0<=x1 and x1<=m-1 and 0<=y1 and y1<=n-1:
            if graph[y1][x1]==0:
                
                cnt+=1
                queue.append((y1,x1,direction))
            else:
                queue.append((y,x,direction))

print(cnt)