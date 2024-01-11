import sys
input=sys.stdin.readline
MAX=sys.maxsize
from heapq import heappush,heappop

def dijkstra(start):
    pq=[]
    heappush(pq,(0,0,start))
    while pq:
        w,cnt,cur=heappop(pq)
        flag=False
        for i in range(cnt):
            if dis[i][cur]<w:
                flag=True
                break
        if cnt==n or flag:
            continue
        
        for neighbor,w1 in graph[cur]:
            if dis[cnt+1][neighbor]>w+w1:
                dis[cnt+1][neighbor]=w+w1
                heappush(pq,(w+w1,cnt+1,neighbor))

def minCost(n,end,taxes):
    ans=MAX
    for i in range(1,n):
        ans=min(ans,dis[i][end]+i*taxes)
    return ans
                

n,m,k=map(int,input().split())
start,end=map(int,input().split())
graph=[[] for _ in range(n+1)]
for j in range(m):
    n1,n2,w=map(int,input().split())
    graph[n1].append((n2,w))
    graph[n2].append((n1,w))

dis=[[MAX]*(n+1) for _ in range(n+1)]

dis[0][start]=0
dijkstra(start)

taxes=0
print(minCost(n,end,taxes))
   
for i in range(k):
    taxes+=int(input())
    print(minCost(n,end,taxes))