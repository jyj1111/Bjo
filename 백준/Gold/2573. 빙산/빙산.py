import sys,copy
from collections import deque
input=sys.stdin.readline
N,M=map(int,input().split())# 3 <= N,M <= 300
dy=[-1,0,1,0]
dx=[0,1,0,-1]
boards=[list(map(int,input().split())) for _ in range(N)]

def areaCnt():
    global boards
    visited=[[0]*(M) for _ in range(N)]
    area=0
    for y in range(N):
        for x in range(M):
            if boards[y][x]>0 and not visited[y][x]:
                area+=1
                queue=deque()
                queue.append([y,x])
                visited[y][x]=1
                while queue:
                    y1,x1=queue.popleft()
                    for k in range(4):
                      y2=y1+dy[k]
                      x2=x1+dx[k]
                      if 0<=y2<N and 0<=x2<M and boards[y2][x2]>0 and not visited[y2][x2]:
                          visited[y2][x2]=1
                          queue.append([y2,x2])
                        
    #print(area)
    return area                
                
                


def melt():
    global boards
    boards1=copy.deepcopy(boards)
    for y in range(N):
        for x in range(M):
            if boards1[y][x]>0:
                for k in range(4):
                    y1=y+dy[k]
                    x1=x+dx[k]
                    if 0<=y1<N and 0<=x1<M and boards1[y1][x1]==0:
                        boards[y][x]=max(boards[y][x]-1,0)

time=0
while True:
    if areaCnt()>=2:
        print(time)
        break
    if areaCnt()==0:
        print(0)
        break
    
    melt()
    time+=1