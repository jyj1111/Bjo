import sys
input=sys.stdin.readline

from collections import deque
dy=[-1,-1,0,1,1,1,0,-1]
dx=[0,1,1,1,0,-1,-1,-1]
while True:
    w,h=map(int,input().split())## w,h은 50이하
    if w==0 and h==0:
        break
    graph=[list(map(int,input().split())) for _ in range(h)]## 1은 땅 0은 바다
    cnt=0
    visited=[[0]*(w) for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if graph[i][j]==1 and visited[i][j]==0:
                queue=deque()
                queue.append([i,j])
                visited[i][j]=1
                while queue:
                    [y,x]=queue.popleft()
                    for k in range(8):
                        y1=y+dy[k]
                        x1=x+dx[k]
                        if 0<=x1<w and 0<=y1<h:
                            if graph[y1][x1]==1 and visited[y1][x1]==0:
                                queue.append([y1,x1])
                                visited[y1][x1]=1

                cnt+=1


    print(cnt)