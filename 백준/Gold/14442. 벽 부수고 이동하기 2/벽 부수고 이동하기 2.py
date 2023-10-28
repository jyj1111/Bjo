import sys
from collections import deque
input=sys.stdin.readline
N,M,K=map(int,input().split())# 1 <= N,M <= 1000, 1<=K=<10
dy=[-1,0,1,0]
dx=[0,1,0,-1]
Boards=[list(map(int,input().rstrip('\n'))) for _ in range(N)]# 0은 이동가능, 1은 장애물
visited=[[[0]*(K+1) for _ in range(M)] for _ in range(N)]
#print(Boards)

def BFS():
    queue=deque()
    queue.append((0,0,0))
    visited[0][0][0]=1
    while queue:
        y,x,power=queue.popleft()
        #print(visited)
        if y==N-1 and x==M-1:
            print(visited[y][x][power])
            return
        for k in range(4):
            y1=y+dy[k]
            x1=x+dx[k]
            if 0<=y1<N and 0<=x1<M and Boards[y1][x1]==0 and not visited[y1][x1][power]:
                visited[y1][x1][power]=visited[y][x][power]+1
                queue.append((y1,x1,power))
        if power<K:
            for k in range(4):
                y1=y+dy[k]
                x1=x+dx[k]
                if 0<=y1<N and 0<=x1<M and Boards[y1][x1]==1 and not visited[y1][x1][power+1]:
                    visited[y1][x1][power+1]=visited[y][x][power]+1
                    queue.append((y1,x1,power+1))


    print(-1)

BFS()
                    