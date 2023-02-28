import sys
input=sys.stdin.readline
n=int(input())
m=int(input())
INF=sys.maxsize
graph=[[INF]*(n+1) for i in range(n+1)]
for i in range(1,n+1):
    graph[i][i]=0
for i in range(m):
    u,v,w=map(int,input().split())
    graph[u][v]=min(graph[u][v],w)
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])
    
for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j]==INF:
            print(0,end=' ')
        else:
            print(graph[i][j],end=' ')

    print()
        