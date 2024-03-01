import sys
from heapq import heappush,heappop
input=sys.stdin.readline
INF=10**7+1

def dijkstra(start):
    pq=[]
    dis=[INF]*(n+1)
    dis[start]=0
    heappush(pq,(start,0))
    while pq:
        cur,w=heappop(pq)
        if w>dis[cur]:
            continue
        for node,w1 in graph[cur]:
            dis1=w+w1
            if dis[node]>dis1:
                dis[node]=dis1
                heappush(pq,(node,dis1))
                
    total,maxDis=0,0
    for i in range(1,n+1):
        if dis[i]!=INF:
            total+=1
            maxDis=max(maxDis,dis[i])
    print(total,maxDis)
           
    
    

for _ in range(int(input())):
    n,d,c=map(int,input().split())
    graph=[[] for _ in range(n+1)]
    for _ in range(d):
        a,b,s=map(int,input().split())
        graph[b].append((a,s))
    dijkstra(c)