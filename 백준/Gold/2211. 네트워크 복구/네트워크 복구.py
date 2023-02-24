import sys
import heapq
input=sys.stdin.readline
INF = sys.maxsize
n,m=map(int,input().split())
graph=[[] for i in range(n+1)]
dis=[INF]*(n+1)

for i in range(m):
    u,v,w=map(int,input().split())
    graph[u].append((w,v))
    graph[v].append((w,u))

answer=[]
cnt=0;
pq=[]
dis[1]=0;
heapq.heappush(pq,(0,1))
while pq:
  
  wei,now=heapq.heappop(pq);
  if dis[now]<wei:
      continue
  for w,neighbor in graph[now]:
      neighbor_wei=wei+w
      if neighbor_wei<dis[neighbor]:
          dis[neighbor]=neighbor_wei
          for j in range(len(answer)):
              if neighbor==answer[j][1]:
                  del(answer[j])
                  cnt-=1
                  break
          answer.append([now,neighbor])
          cnt+=1
          heapq.heappush(pq,(neighbor_wei,neighbor))

print(cnt)
for x,y in answer:
    print(x,y)