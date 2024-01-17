import sys,copy
from collections import deque
input=sys.stdin.readline

m,n=map(int,input().split())
graph=[list(map(int,list(input().rstrip('\n')))) for _ in range(m)]

def bfs(i,j,visited):
    queue=deque()
    queue.append((i,j))
    visited[i][j]=1
    while queue:
        y,x=queue.popleft()
        for dy,dx in [(-1,0),(0,1),(1,0),(0,-1)]:
            y1=y+dy
            x1=x+dx
            if 0<=y1<m and 0<=x1<n and graph[y1][x1] and not visited[y1][x1]:
                visited[y1][x1]=1
                queue.append((y1,x1))
 
def check():
    visited=[[0]*(n) for _ in range(m)]
    cnt=0
    for i in range(m):
        for j in range(n):
            if graph[i][j]>0 and not visited[i][j]:
                bfs(i,j,visited)
                cnt+=1
    #print(visited)
    #print(cnt)                
    return cnt
    

cnt=check()
ans=0
graph1=copy.deepcopy(graph)
while cnt!=1:
    for i in range(m):
        for j in range(n):
            if graph[i][j]>0:
                k=graph[i][j]
                for y in range(i-k,i+k+1):
                    for x in range(j-k,j+k+1):
                        if 0<=y<m and 0<=x<n:
                            graph1[y][x]=max(graph1[y][x],k)
         
    for i in range(m):
        for j in range(n):
            graph[i][j]=graph1[i][j]
                            
    cnt=check()
    ans+=1

print(ans)