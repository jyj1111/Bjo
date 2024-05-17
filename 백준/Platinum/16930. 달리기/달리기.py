import sys
from collections import deque
input=sys.stdin.readline
n,m,k=map(int,input().split())
graph=[list(input().rstrip('\n')) for _ in range(n)]
x0,y0,x1,y1=map(int,input().split())

queue=deque()
queue.append((x0-1,y0-1))
visited=[[-1]*(m) for _ in range(n)]
visited[x0-1][y0-1]=0
while queue:
    x,y=queue.popleft()
    for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
        for dis in range(1,k+1):
            x2,y2=x+dx*dis,y+dy*dis
            if 0>x2 or x2>=n or  0>y2 or y2>=m:
                break
            if graph[x2][y2]=='#':
                break
            if visited[x2][y2]==-1:
                visited[x2][y2]=visited[x][y]+1
                queue.append((x2,y2))
            elif visited[x][y]>=visited[x2][y2]:
                break
            
print(visited[x1-1][y1-1])