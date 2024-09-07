import sys,math
from collections import deque

n,k=map(int,input().split())

points=[(0,0)]
for _ in range(n):
    x,y=map(int,input().split())
    points.append((x,y))

points.append((10000,10000))

fuels=[[0]*(n+2) for _ in range(n+2)]

def fuel(x,y,x1,y1):
    return math.ceil(((x-x1)**2+(y-y1)**2)**0.5/10)

for i in range(n+2):
    x,y=points[i]
    for j in range(n+2):
        x1,y1=points[j]
        fuels[i][j]=fuel(x,y,x1,y1)


def bfs(dis):
    visited=[False]*(n+2)
    visited[0]=True
    queue=deque()
    queue.append((0,0))
    while queue:
        cur,cnt=queue.popleft()
        if fuels[cur][n+1]<=dis:
            return True
        if cnt>=k:
            continue

        for node in range(n+2):
            if node!=cur and not visited[node] and fuels[cur][node]<=dis:
                visited[node]=True
                queue.append((node,cnt+1))

    return False


l,r=0,1415
ans=0

while l<=r:
    mid=(l+r)//2
    if bfs(mid):
        ans=mid
        r=mid-1
    else:
        l=mid+1

print(ans)