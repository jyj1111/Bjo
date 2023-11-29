import sys
input=sys.stdin.readline
INF=sys.maxsize
n,m=map(int,input().split())
graph=[]
dis=[INF]*(n+1)
dis[1]=0
for i in range(m):
    start,end,cost=map(int,input().split())
    graph.append((start,end,cost))

negativeCycle=False

for i in range(n-1):
    for j in range(m):
        start,end,cost=graph[j]
        if dis[start]!=INF and dis[end]>dis[start]+cost:
            dis[end]=dis[start]+cost

for j in range(m):
    start,end,cost=graph[j]
    if dis[start]!=INF and dis[end]>dis[start]+cost:
        negativeCycle=True
        break

if negativeCycle:
    print(-1)
else:
    for i in range(2,n+1):
        if dis[i]==INF:
            print(-1)
        else:
            print(dis[i])