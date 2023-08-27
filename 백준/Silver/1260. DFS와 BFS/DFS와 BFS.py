import sys
input=sys.stdin.readline
from collections import defaultdict,deque
N,M,V=map(int,input().split())## N은 1000이하, M은 10000이하,
graph=defaultdict(list)
for i in range(M):
    v1,v2=map(int,input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
    graph[v1].sort()
    graph[v2].sort()
    
dfs=[]
dfs.append(str(V))
visitiedDFS=[0 for _ in range(N+1)]
visitiedDFS[V]=1

def DFS(start):
    
    for nei in graph[start]:
        if not visitiedDFS[nei]:
            visitiedDFS[nei]=1
            dfs.append(str(nei))
            DFS(nei)
            
DFS(V)
print(' '.join(dfs))

bfs=[]
bfs.append(str(V))
visitiedBFS=[0 for _ in range(N+1)]
visitiedBFS[V]=1

def BFS(start):
    queue=deque()
    queue.append(start)
    while queue:
        
        v=queue.popleft()
       
        for nei in graph[v]:
            if not visitiedBFS[nei]:
                visitiedBFS[nei]=1
                bfs.append(str(nei))
                queue.append(nei)

BFS(V)
print(' '.join(bfs))