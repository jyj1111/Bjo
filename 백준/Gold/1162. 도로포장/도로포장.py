import sys,heapq
from collections import defaultdict
input=sys.stdin.readline
INF=sys.maxsize
n,e,k=map(int,input().split())

dis=[[INF]*(n+1) for _ in range(k+1)]
dis[0][1]=0

graph=defaultdict(list)

for i in range(e):
    n1,n2,w=map(int,input().split())
    graph[n1].append((n2,w))
    graph[n2].append((n1,w))

pq=[]
pq.append((0,1,0))
heapq.heapify(pq)
ans=INF

while pq:
    
    w,cur,wrap=heapq.heappop(pq)
    if dis[wrap][cur]<w:
        continue
    if cur==n:
        ans=min(ans,dis[wrap][cur])
    
    for neighbor,w1 in graph[cur]:
        if dis[wrap][neighbor]>w+w1:
            dis[wrap][neighbor]=w+w1
            heapq.heappush(pq,(w+w1,neighbor,wrap))
            if wrap<k and dis[wrap+1][neighbor]>w:
                dis[wrap+1][neighbor]=w
                heapq.heappush(pq,(w,neighbor,wrap+1))


print(ans)