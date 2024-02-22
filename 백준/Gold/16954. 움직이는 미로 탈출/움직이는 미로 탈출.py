import sys
from collections import deque
input=sys.stdin.readline

Maps=[list(input().strip('\n')) for _ in range(8)]
dy=[0,-1,0,1,0,-1,-1,1,1]
dx=[0,0,1,0,-1,1,-1,-1,1]

def inbound(y,x):
    if 0<=y<8 and 0<=x<8:
        return True
    return False

queue=deque()
queue.append((7,0))
visited=[[False]*(8) for _ in range(8)]
visited[7][0]=True
ans=0

while queue:
    
    y,x=queue.popleft()
    if y==0:
        ans=1
        break
    
    for i in range(9):
        y1,x1=y+dy[i],x+dx[i]
        if inbound(y1,x1) and Maps[y1][x1]=='.':
            if Maps[y1-1][x1]=='.' and not visited[y1-1][x1]:
                visited[y1-1][x1]=True
                queue.append((y1-1,x1))

    

print(ans)