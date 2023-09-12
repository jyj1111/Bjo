import sys
input=sys.stdin.readline
from collections import deque
N,L,R=map(int,input().split()) #N<=50,L<=100,R<=100
graph=[list(map(int,input().split())) for _ in range(N)]

ans=0
dy=[-1,0,1,0]
dx=[0,1,0,-1]

while True:
    
    visited=[[0]*N for _ in range(N)]
    #print(graph)
    flag=False
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                queue=deque()
                
                arr=[]
                queue.append([i,j])
                arr.append([i,j])
                visited[i][j]=1
                hap=graph[i][j]
                while queue:
                    #print(queue)
                    y,x=queue.popleft()
                    for k in range(4):
                        y1=y+dy[k]
                        x1=x+dx[k]
                        if 0<=x1<N and 0<=y1<N and not visited[y1][x1]:
                            if L<=abs(graph[y1][x1]-graph[y][x])<=R:
                                visited[y1][x1]=1
                                queue.append([y1,x1])
                                arr.append([y1,x1])
                                hap+=graph[y1][x1]
                                flag=True
       
                #print(arr)       
                if len(arr)==1:
                    visited[i][j]=0
                else:
                    for i1,j1 in arr:
                        graph[i1][j1]=hap//len(arr)              
                
    if not flag:
        break
    ans+=1


print(ans)
