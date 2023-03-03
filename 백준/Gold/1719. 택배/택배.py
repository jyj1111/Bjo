import sys
input=sys.stdin.readline
INF = sys.maxsize
n,m=map(int,input().split())
graph=[[INF]*(n+1) for i in range(n+1)]
for i in range(1,n+1):
    graph[i][i]=0
arr=[['-']*(n+1) for i in range(n+1)]
for i in range(m):
    u,v,w=map(int,input().split())
    graph[u][v]=w
    graph[v][u]=w
    arr[v][u]=u
    arr[u][v]=v
    


for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i==j:
                continue
            
            if graph[i][j]>graph[i][k]+graph[k][j]:
                graph[i][j]=graph[i][k]+graph[k][j]
                arr[i][j]=arr[i][k]
            
                
for i in range(1,n+1):

    for j in range(1,n+1):
        print(arr[i][j],end=' ')

    print()