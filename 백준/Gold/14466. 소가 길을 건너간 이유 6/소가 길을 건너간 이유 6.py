import sys,math
input=sys.stdin.readline
from collections import deque,defaultdict
from itertools import combinations

n,k,r=map(int,input().split())

roads=defaultdict(list)
cows=defaultdict(int)

def bfs(y,x):
    visited=[[0]*(n+1) for _ in range(n+1)]
    queue=deque()
    queue.append((y,x))
    visited[y][x]=1
    #print(visited)
    #print(cows)
    #print(roads)
    while queue:
        y1,x1=queue.popleft()
        if (y1,x1) in cows and (y1!=y or x1!=x):
            cows[(y,x)]+=1
            #print(y1,x1)
        for dy,dx in [(-1,0),(0,1),(1,0),(0,-1)]:
            y2=y1+dy
            x2=x1+dx
            if y2<=0 or y2>n:
                continue
            if x2<=0 or x2>n:
                continue
            if (y2,x2) in roads[(y1,x1)]:
                continue
            if visited[y2][x2]:
                continue
            visited[y2][x2]=1
            queue.append((y2,x2))
    #print(y,x,cows[(y,x)])        
    return cows[(y,x)]
                 
   

for i in range(r):
    y1,x1,y2,x2=map(int,input().split())
    roads[(y1,x1)].append((y2,x2))
    roads[(y2,x2)].append((y1,x1))

for i in range(k):
    y,x=map(int,input().split())
    cows[(y,x)]=0

ans=k*(k-1)
for y,x in cows:
    ans-=bfs(y,x)


print(ans//2)
    