import sys
from collections import deque,defaultdict
input=sys.stdin.readline

n,m=map(int,input().split())
graph=defaultdict(list)

for i in range(m):
    x,y,a,b=map(int,input().split())
    graph[(x,y)].append((a,b))
    

def bfs():
    queue=deque()
    queue.append((1,1))
    visited=[[0]*(n+1) for _ in range(n+1)]
    visited[1][1]=1
    lighted=[[0]*(n+1) for _ in range(n+1)]
    lighted[1][1]=1
    ans=1
    while queue:
        x,y=queue.popleft()
        for x1,y1 in graph[(x,y)]:
            if not lighted[x1][y1]:
                lighted[x1][y1]=1
                ans+=1
                if visited[x1][y1]:
                    queue.append((x1,y1))

        for dx,dy in [(-1,0),(0,1),(0,-1),(1,0)]:
            x1=x+dx
            y1=y+dy
            if 1<=x1<=n and 1<=y1<=n and not visited[x1][y1]:
                visited[x1][y1]=1
                if lighted[x1][y1]:
                    queue.append((x1,y1))
            
                
    return ans
 

print(bfs())    