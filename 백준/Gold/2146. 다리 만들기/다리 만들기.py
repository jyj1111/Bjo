import sys
from collections import deque
input=sys.stdin.readline

n=int(input()) # n<=100
maps=[list(map(int,input().split())) for _ in range(n)]# 0은 바다, 1은 육지
visited=[[0]*(n) for _ in range(n)]
Area=[]

def BFS(i,j):
    global cnt,visited,Area
    queue=deque()
    area=[]
    queue.append((i,j))
    visited[i][j]=cnt
    while queue:
        y,x=queue.popleft()
        area.append((y,x))
        for dy,dx in [(-1,0),(0,1),(1,0),(0,-1)]:
            y1=y+dy
            x1=x+dx
            
            if 0<=y1<n and 0<=x1<n and maps[y1][x1]==1 and not visited[y1][x1]:
                queue.append((y1,x1))
                visited[y1][x1]=cnt
    Area.append(area)
                     
    

cnt=0
for i in range(n):
    for j in range(n):
        if maps[i][j]==1 and not visited[i][j]:
            cnt+=1
            BFS(i,j)
#print(Area)

if len(Area)==1:
    print(0)
else:
    dis=2*(n-1)
    for i in range(cnt-1):
        for j in range(i+1,cnt):
            for y1,x1 in Area[i]:
                for y2,x2 in Area[j]:
                    dis=min(dis,abs(y1-y2)+abs(x1-x2)-1)
                    #print(dis)
print(dis)