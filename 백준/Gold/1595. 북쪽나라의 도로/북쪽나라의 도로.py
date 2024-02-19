import sys
input=sys.stdin.readline
from collections import defaultdict,deque

maps=defaultdict(list)

def BFS(root):
    global ans
    queue=deque()
    visited=[0]*(10001)
    visited[root]=1
    queue.append((root,0))
    while queue:
        node,dis=queue.popleft()
        ans=max(ans,dis)
        for neighbor,w in maps[node]:
            if not visited[neighbor]:
                visited[neighbor]=1
                queue.append((neighbor,dis+w))

while True:
    try:
        
        n1,n2,w=map(int,input().split())
        maps[n1].append((n2,w))
        maps[n2].append((n1,w))
        
    except:
        break
    
       
 
ans=0 

for root in maps:
    BFS(root)

print(ans)