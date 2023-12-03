from collections import deque
def solution(n, edge):
    answer = 0
    graph=[[] for _ in range(n+1)]
    
    for n1,n2 in edge:
        graph[n1].append(n2)
        graph[n2].append(n1)
    visited=[0]*(n+1)
    queue=deque()
    queue.append(1)
    visited[1]=1
    maxDis=1
    while queue:
        node=queue.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor]=visited[node]+1
                maxDis=max(maxDis,visited[neighbor])
        
    return visited.count(maxDis)