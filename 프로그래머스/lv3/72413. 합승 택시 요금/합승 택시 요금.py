"""
3<=n<=200
2<=fares의 길이<=n*(n-1)/2
"""
import heapq,sys
from collections import defaultdict
INF=sys.maxsize
def solution(n, s, a, b, fares):
    answer = 0
    costs=[[INF]*(n+1) for _ in range(n+1)]
    graph=defaultdict(list)
    for i in range(1,n+1):
        costs[i][i]=0
    for c,d,f in fares:
        graph[c].append((d,f))
        graph[d].append((c,f))
           
    for i in range(1,n+1):
        pq=[]
        heapq.heapify(pq)
        heapq.heappush(pq,(0,i))
        while pq:
            #print(pq)
            cost,node=heapq.heappop(pq)
            if costs[i][node]<cost:
                continue
            for neighbor,worth in graph[node]:
                cost1=cost+worth
                if cost1<costs[i][neighbor]:
                    costs[i][neighbor]=cost1
                    heapq.heappush(pq,(cost1,neighbor))
       
    answer=costs[s][a]+costs[s][b]
    for i in range(1,n+1):
        answer=min(answer,costs[s][i]+costs[i][a]+costs[i][b])
        
    
    return answer