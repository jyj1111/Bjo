import sys
input=sys.stdin.readline
MAX=sys.maxsize
from heapq import heappush,heappop

def dijkstra(start,end):
    dis=[MAX]*(n+1)
    dis[start]=0
    pq=[]
    heappush(pq,(0,start))
    while pq:
        w,cur=heappop(pq)
        if w>dis[cur]:
            continue
        for neighbor,w1 in graph[cur]:
            if dis[neighbor]>w+w1:
                dis[neighbor]=w+w1
                heappush(pq,(w+w1,neighbor))
                
    return dis[end]

T=int(input())
for i in range(T):
    n,m,t=map(int,input().split())
    s,g,h=map(int,input().split())
    graph=[[] for _ in range(n+1)]
    for j in range(m):
        n1,n2,w=map(int,input().split())
        graph[n1].append((n2,w))
        graph[n2].append((n1,w))

    answer=[]
    for j in range(t):
        e=int(input())
        dis=dijkstra(s,e)
        if dis==dijkstra(s,g)+dijkstra(g,e) and dis==dijkstra(s,h)+dijkstra(h,e):
            answer.append(e)
 
    answer.sort()
    print(*answer)