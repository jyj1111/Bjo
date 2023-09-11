import sys
input=sys.stdin.readline
from collections import deque
dy=[-1,0,1,0]
dx=[0,1,0,-1]
y,x=map(int,input().split())## y,x은 50이하
arr=[list(input().rstrip('\n')) for _ in range(y)]##L은 육지, W은 바다

ans=0

for i in range(y):
    for j in range(x):
        if arr[i][j]=='L':
            queue=deque()
            visited=[[0]*x for _ in range(y)]
            visited[i][j]=1
            queue.append([i,j])
            while queue:
                y1,x1=queue.popleft()
                for k in range(4):
                    y2=y1+dy[k]
                    x2=x1+dx[k]
                    if 0<=x2<x and 0<=y2<y:
                      if not visited[y2][x2] and arr[y2][x2]=='L':
                          visited[y2][x2]=visited[y1][x1]+1
                          queue.append([y2,x2])
            #print(visited)
            ans=max(ans,max(map(max,visited)))
                          
print(ans-1)