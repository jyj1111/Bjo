import sys
input=sys.stdin.readline
from heapq import heappush,heappop
MAX=sys.maxsize
w,h=map(int,input().split())
graph=[list(input().rstrip('\n')) for _ in range(h)]
dy=[0,-1,0,1,0]
dx=[0,0,1,0,-1]

rasers=[]

for i in range(h):
    for j in range(w):
        if graph[i][j]=='C':
            rasers.append((i,j))

start,end=rasers


def BFS(start,end):
    pq=[]
    visited=[[[[0]*(5) for _ in range(5)] for _ in range(w)] for _ in range(h)]
    y,x=start
    heappush(pq,(0,0,y,x))
    visited[y][x][0][0]=1
    ans=MAX
    while pq:
        cnt,direction,y1,x1=heappop(pq)
        #print(y1,x1,direction,cnt)
        for k in range(1,5):
            y2=y1+dy[k]
            x2=x1+dx[k]
            flag=0
            if direction>0 and direction!=k:
                flag=1
                
            if y2==end[0] and x2==end[1]:
                if flag:
                     ans=min(ans,cnt+1)
                else:
                     ans=min(ans,cnt)
                return ans
                    
               
            if 0<=y2<h and 0<=x2<w and not visited[y2][x2][direction][k] and graph[y2][x2]=='.':
                visited[y2][x2][direction][k]=1
                if flag:
                    heappush(pq,(cnt+1,k,y2,x2))
                    
                else:
                    heappush(pq,(cnt,k,y2,x2))
             
 


print(BFS(start,end))