import heapq
from collections import defaultdict
def solution(n, roads, sources, destination):
    answer = []
    MAX=100001
    dis=[MAX]*(n+1)
    dis[destination]=0
    pq=[(0,destination)]
    heapq.heapify(pq)
    graph=defaultdict(list)
    for node1,node2 in roads:
        graph[node1].append((node2,1))
        graph[node2].append((node1,1))
    
    while pq:
        w,node=heapq.heappop(pq)
        for neighbor,weight in graph[node]:
            if dis[neighbor]>dis[node]+weight:
                dis[neighbor]=dis[node]+weight
                heapq.heappush(pq,(dis[neighbor],neighbor))
                
    for source in sources:
        if dis[source]==MAX:
            answer.append(-1)
        else:
            answer.append(dis[source])
        
    return answer