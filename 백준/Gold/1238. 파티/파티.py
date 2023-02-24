import sys
import heapq
input=sys.stdin.readline
INF = sys.maxsize
n,m,x=map(int,input().split())
graph=[[] for i in range(n+1)]
dis=[[INF]*(n+1) for i in range(n+1)]

for i in range(m):
    u,v,w=map(int,input().split())
    graph[u].append((w,v))


for i in range(1,n+1):
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

              
answer=0
for i in range(1,n+1):
    if i==x:
        continue;
    answer=max(answer,dis[i][x]+dis[x][i])

print(answer)