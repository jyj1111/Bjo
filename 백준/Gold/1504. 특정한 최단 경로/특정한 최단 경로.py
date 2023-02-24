import sys
import heapq
input=sys.stdin.readline
INF = sys.maxsize
n,e=map(int,input().split())
graph=[[] for i in range(n+1)]
dis=[[INF]*(n+1) for i in range(n+1)]

for i in range(e):
    u,v,w=map(int,input().split())
    graph[u].append((w,v))
    graph[v].append((w,u))
    
x1,x2=map(int,input().split())

for i in [1,x1,x2,n]:
    pq=[]
    dis[i][i]=0;
    heapq.heappush(pq,(0,i))
    while pq:
      wei,now=heapq.heappop(pq);
      if dis[i][now]<wei:
          continue
      for w,neighbor in graph[now]:
          neighbor_wei=wei+w
          if neighbor_wei<dis[i][neighbor]:
              dis[i][neighbor]=neighbor_wei
              heapq.heappush(pq,(neighbor_wei,neighbor))

              
path1=dis[1][x1]+dis[x1][x2]+dis[x2][n]
path2=dis[1][x2]+dis[x2][x1]+dis[x1][n]

answer=min(path1,path2)
if answer>=INF:
    print(-1)
else:
    print(answer)