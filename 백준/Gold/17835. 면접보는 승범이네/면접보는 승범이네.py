import sys
import heapq
input=sys.stdin.readline
INF = sys.maxsize
n,m,k=map(int,input().split())
graph=[[] for i in range(n+1)]
for i in range(m):
    u,v,w=map(int,input().split())
    graph[v].append((w,u))

interviews=list(map(int,input().split()))
dis=[INF]*(n+1)
pq=[]
for interview in interviews:
    dis[interview]=0
    heapq.heappush(pq,(0,interview))
    
while pq:
    wei,now=heapq.heappop(pq);
    if dis[now]<wei:
        continue  
    for w,neighbor in graph[now]:
        neighbor_wei=wei+w
        if neighbor_wei<dis[neighbor]:
            dis[neighbor]=neighbor_wei
            heapq.heappush(pq,(neighbor_wei,neighbor))
        
ans=0
idx=0
for i in range(1,n+1):
    if dis[i]>ans:
        ans=dis[i]
        idx=i
print(idx)
print(ans)