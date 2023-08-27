import sys
input=sys.stdin.readline
from collections import deque
inf=sys.maxsize
n,m=map(int,input().split())## n,m은 1000이하 0은 이동가능, 1인 이동 불가
graph=[list(map(int,input().rstrip('\n'))) for _ in range(n)]
visited=[[[0]*(2) for _ in range(m)] for _ in range(n)]
visited[0][0][0]=1
queue=deque()
queue.append([0,0,0])
dy=[-1,0,1,0]
dx=[0,1,0,-1]
ans=1
crashNum=0 ## 1까지는 허용 
arrived=False
while queue:
    y,x,crashed=queue.popleft()
    if y==n-1 and x==m-1:
        arrived=True
        break
    for i in range(4):
        y1=y+dy[i]
        x1=x+dx[i]
        if 0<=y1<n and 0<=x1<m:
            if visited[y1][x1][crashed]==0 and graph[y1][x1]==0:
                visited[y1][x1][crashed]=visited[y][x][crashed]+1
                queue.append([y1,x1,crashed])
            elif visited[y1][x1][crashed]==0 and graph[y1][x1]==1:
                if crashed==1:
                    continue
                else:
                    crashNum=1
                    visited[y1][x1][1]=visited[y][x][0]+1
                    queue.append([y1,x1,1])

if arrived:
     print(visited[n-1][m-1][crashNum])
else:
    print(-1)