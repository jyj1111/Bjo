## intensity:휴식 없이 이동해야 하는 시간 중 가장 긴 시간
## n: XX산의 지점 수
## paths: 각 등산로의 정보를 담은 2차원 정수 배열 [i, j, w]
## gates: 출입구들의 번호가 담긴 정수 배열
## summits: 산봉우리들의 번호
## answer:[산봉우리 번호중 제일 낮은것, intensity 최솟값]
import heapq
import sys
from collections import defaultdict
INF=sys.maxsize
def solution(n, paths, gates, summits):
    dis=[INF]*(n+1) 
    graph=defaultdict(list)
    pq=[]
    summits.sort()
    summit_set=set(summits)
    for path in paths:
        i,j,w=path
        graph[i].append((w,j))
        graph[j].append((w,i))
    for gate in gates:
        dis[gate]=0
        heapq.heappush(pq,(0,gate))
    while pq:
        intensity,node=heapq.heappop(pq)
        if node in summit_set or intensity>dis[node]:
            continue
        for weight, next_node in graph[node]:
            new_intensity = max(intensity,weight)  
            if new_intensity < dis[next_node]:
                dis[next_node] = new_intensity
                heapq.heappush(pq, (new_intensity, next_node))
               
    min_intensity = [0,INF]
    for summit in summits:
        if dis[summit] < min_intensity[1]:
            min_intensity[0] = summit
            min_intensity[1] = dis[summit]

    return min_intensity            
        
    
    
    
    
    
    
    
    
    