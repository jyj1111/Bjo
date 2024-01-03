import sys
from collections import defaultdict
from heapq import heappop,heappush
input=sys.stdin.readline
MAX=sys.maxsize
n,m=map(int,input().split())

graph=[[] for _ in range(n+1)]

for time in range(1,m+1):
    n1,n2=map(int,input().split())
    graph[n1].append((n2,time))
    graph[n2].append((n1,time))

dis=[MAX]*(n+1)
dis[1]=0
pq=[]
heappush(pq,(0,1))

while pq:
    w,cur=heappop(pq)
    if w>dis[cur]:
        continue
    for neighbor,w1 in graph[cur]:
        if w>=w1:
            w1+=m*(((w-w1)//m)+1)
  
        if dis[neighbor]>w1:
            dis[neighbor]=w1
            heappush(pq,(w1,neighbor))    
                           
                
            

print(dis[n])