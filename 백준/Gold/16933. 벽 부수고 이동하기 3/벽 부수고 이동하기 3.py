import sys
input=sys.stdin.readline
from collections import deque

n,m,k=map(int,input().split())
graph=[list(input().rstrip('\n')) for _ in range(n)]
ans=-1

queue=deque()
visited=[[[False]*(k+1) for _ in range(m)] for _ in range(n)]
visited[0][0][0]=True
queue.append((0,0,0,0))

while queue:
    y,x,cnt,day=queue.popleft()
    #print(y,x,cnt,day)
    if y==n-1 and x==m-1:
        ans=day
        break

    for dy,dx in [(1,0),(0,1),(-1,0),(0,-1)]:
        y1,x1,cnt1,day1=y+dy,x+dx,cnt+1,day+1
        if 0<=y1<n and 0<=x1<m:
            if graph[y1][x1]=='1' and cnt<k and not visited[y1][x1][cnt1]:
                if day%2==0 :
                    visited[y1][x1][cnt1]=True
                    queue.append((y1,x1,cnt1,day1))
                else:
                  queue.append((y,x,cnt,day1))
  
            elif graph[y1][x1]=='0' and not visited[y1][x1][cnt]:
                visited[y1][x1][cnt]=True
                queue.append((y1,x1,cnt,day1))

print(ans+1 if ans>=0 else -1)
        