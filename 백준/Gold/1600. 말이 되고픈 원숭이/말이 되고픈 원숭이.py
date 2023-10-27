import sys
input=sys.stdin.readline
from collections import deque
"""

"""

K=int(input())# K<=30
W,H=map(int,input().split())# 1<=W,H<=200
Boards=[list(map(int,input().split())) for _ in range(H)]# 0은 평지, 1은 장애물
visited=[[[0]*(K+1) for _ in range(W)] for _ in range(H)]

horseDy=[1,2,2,1,-1,-2,-2,-1]
horseDx=[2,1,-1,-2,-2,-1,1,2]
Dy=[0,1,0,-1]
Dx=[1,0,-1,0]

def BFS():
    queue=deque()
    queue.append((0,0,0))
    visited[0][0][0]=1
    while queue:
        y,x,horse=queue.popleft()
        #print(visited)
        #print(y,x,visited[y][x])
        if y==H-1 and x==W-1:
            print(visited[y][x][horse]-1)
            return
        if horse<K:
             for k in range(8):
                y1=y+horseDy[k]
                x1=x+horseDx[k]
                if 0<=y1<H and 0<=x1<W and Boards[y1][x1]==0 and not visited[y1][x1][horse+1]:
                
                    visited[y1][x1][horse+1]=visited[y][x][horse]+1
                    queue.append((y1,x1,horse+1))
            
       
        
        for k in range(4):
            y1=y+Dy[k]
            x1=x+Dx[k]
            if 0<=y1<H and 0<=x1<W and Boards[y1][x1]==0 and not visited[y1][x1][horse]:
                visited[y1][x1][horse]=visited[y][x][horse]+1
                
                queue.append((y1,x1,horse))
                    
    
    print(-1)

BFS()