import sys
import heapq
input=sys.stdin.readline
n,m=map(int,input().split())
k=int(input())
INF = sys.maxsize
dis=[INF]*(n+1)

graph=[[] for i in range(n+1)]
pq=[]
for i in range(m):
    u,v,w=map(int,input().split())
    graph[u].append((w,v))

dis[k]=0;
heapq.heappush(pq,(0,k))

while pq:
    
    wei,now=heapq.heappop(pq);
    if dis[now]<wei:
        continue
    for w,neighbor in graph[now]:
        neighbor_wei=wei+w
        if neighbor_wei<dis[neighbor]:
            dis[neighbor]=neighbor_wei
            heapq.heappush(pq,(neighbor_wei,neighbor))

                    
for i in range(1,n+1):
    if dis[i]==INF:
        print("INF")
    else:
        print(dis[i])
                
                
                
                
                
            
                
                
            
            
        
      
    
    
    