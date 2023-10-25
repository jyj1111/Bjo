import sys
from collections import deque
input=sys.stdin.readline

n,m=map(int,input().split()) # n,m<=10
maps=[list(map(int,input().split())) for _ in range(n)]# 0은 바다, 1은 육지
visited=[[0]*(m) for _ in range(n)]
Area=[]

def find(x):
    if parents[x]!=x:
        parents[x]=find(parents[x])
    return parents[x]

def union(i,j):
    i=find(i)
    j=find(j)
    if i<j:
        parents[j]=i
    else:
        parents[i]=j
    

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
            
            if 0<=y1<n and 0<=x1<m and maps[y1][x1]==1 and not visited[y1][x1]:
                queue.append((y1,x1))
                visited[y1][x1]=cnt
    
    Area.append(area)
    
cnt=0
for i in range(n):
    for j in range(m):
        if maps[i][j]==1 and not visited[i][j]:
            cnt+=1
            BFS(i,j)
            
            
#print(Area)
parents=[i for i in range(cnt)]
Edges=[]

for i in range(cnt-1):
    for j in range(i+1,cnt):
        dis=n+m
        flag=False
        for y1,x1 in Area[i]:
            for y2,x2 in Area[j]:
                In=False
                if y1!=y2 and x1!=x2:
                    continue
                elif y1==y2 and x1!=x2:
                    dx=1
                    if x2<x1:
                        dx=-dx                        
                    for j1 in range(x1+dx,x2,dx):
                        if visited[y1][j1]>0:
                            In=True
                            break
                    
                elif y1!=y2 and x1==x2:
                    dy=1
                    if y2<y1:
                        dy=-dy   
                    for i1 in range(y1+dy,y2,dy):
                        if visited[i1][x1]>0:
                            In=True
                            break
                if In:
                    continue
                    
                dis1=abs(y1-y2)+abs(x1-x2)-1
                if dis1<2:
                    continue
                
                if dis1<dis:
                    flag=True
                    dis=min(dis,dis1)
                    
        if flag:
            #print(dis,i,j) 
            Edges.append((dis,i,j)) 
                           
               
            
            

ans=0
edgeCnt=0
Edges.sort()
for dis,i,j in Edges:
    if find(i)==find(j):
        continue
    ans+=dis
    edgeCnt+=1
    union(i,j)
    
if edgeCnt<cnt-1:
    print(-1)
else:
    print(ans)