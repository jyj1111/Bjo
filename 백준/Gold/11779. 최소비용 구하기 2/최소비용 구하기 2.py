import sys
import heapq
input=sys.stdin.readline
INF = sys.maxsize
n=int(input())
m=int(input())
graph=[[] for i in range(n+1)]
dis=[INF]*(n+1)

for i in range(m):
    u,v,w=map(int,input().split())
    graph[u].append((w,v))

start,end=map(int,input().split())    
pq=[]
dis[start]=0;
heapq.heappush(pq,(0,start,[start]))
midVertexs=[]
while pq:
  
  wei,now,path=heapq.heappop(pq);
  if now==end:
      midVertexs=path
      break
  if dis[now]<wei:
      continue
  for w,neighbor in graph[now]:
      neighbor_wei=wei+w
      if neighbor_wei<dis[neighbor]:
          dis[neighbor]=neighbor_wei
          heapq.heappush(pq,(neighbor_wei,neighbor,path+[neighbor]))         
          
print(dis[end])
print(len(midVertexs))
ans=""
for i in midVertexs:
    ans+=str(i)+" "

print(ans.rstrip())