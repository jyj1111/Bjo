import sys
from heapq import heappush,heappop
from collections import defaultdict
MAX=sys.maxsize
input=sys.stdin.readline
t=int(input())

def dijkstra(start):
    pq=[]
    dis=[MAX]*(n+1)
    dis[start]=0
    heappush(pq,(start,0))
    while pq:
        cur,w=heappop(pq)
        if w>dis[cur]:
            continue
        for node,w1 in graph[cur]:
            if dis[node]>w+w1:
                dis[node]=w+w1
                heappush(pq,(node,w+w1))
                
    total,maxDis=0,0
    for i in range(1,n+1):
        if dis[i]!=MAX:
            total+=1
            maxDis=max(maxDis,dis[i])
    print(total,maxDis)
           
    
    

for t1 in range(t):
    n,d,c=map(int,input().split())
    graph=defaultdict(list)
    for j in range(d):
        a,b,s=map(int,input().split())
        graph[b].append((a,s))
        
    dijkstra(c)