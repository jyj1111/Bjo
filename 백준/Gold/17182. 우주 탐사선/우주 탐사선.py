import sys
input=sys.stdin.readline
INF=sys.maxsize
n,start=map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(n)]
    
    
for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][j]>graph[i][k]+graph[k][j]:
                graph[i][j]=graph[i][k]+graph[k][j]
                
                
                
visited=[0]*(n)
ans=sys.maxsize
def DFS(start,cnt,dis):
    global ans
    if cnt==n:
        ans=min(ans,dis)
        return
    else:
        for i in range(n):
            if not visited[i]:
                visited[i]=1
                DFS(i,cnt+1,dis+graph[start][i])
                visited[i]=0


visited[start]=1
DFS(start,1,0)
print(ans)
        