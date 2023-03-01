import sys
input=sys.stdin.readline
INF=sys.maxsize
n,m,r=map(int,input().split())
items=list(map(int,input().split()))
graph=[[INF]*(n+1) for i in range(n+1)]
for i in range(n+1):
    graph[i][i]=0
for i in range(r):
    u,v,w=map(int,input().split())
    graph[u][v]=w
    graph[v][u]=w

for k in range(n+1):
    for u in range(n+1):
        for v in range(n+1):
            graph[u][v]=min(graph[u][v],graph[u][k]+graph[k][v])
            
ans=0
for i in range(1,n+1):
    itemCnt=0
    for j in range(1,n+1):
        if graph[i][j]<=m:
            itemCnt+=items[j-1]
    ans=max(ans,itemCnt)
        
print(ans)    