from collections import deque

def solution(board):
    answer = 0
    n=len(board)
    m=len(board[0])
    startY,startX=-1,-1
    for i in range(n):
        for j in range(m):
            if board[i][j]=='R':
                startY=i
                startX=j
                break
                
    def BFS(startY,startX):
        visited=[[0]*(m) for _ in range(n)]
        queue=deque()
        queue.append((startY,startX))
        visited[startY][startX]=1
        while queue:
            y,x=queue.popleft()
            #print(y,x)
            if board[y][x]=='G':
                return visited[y][x]-1
            for dy,dx in [(-1,0),(0,1),(1,0),(0,-1)]:
                curY,curX=y,x
                while True:
                    y1=curY+dy
                    x1=curX+dx
                    if 0<=y1<n and 0<=x1<m and board[y1][x1]=='D':
                        break
                    elif y1<0 or y1>=n or x1<0 or x1>=m:
                        break
                    curY,curX=y1,x1
                
                if not visited[curY][curX]:
                    visited[curY][curX]=visited[y][x]+1
                    queue.append((curY,curX))
                
        return -1

               
    answer=BFS(startY,startX)
                
    return answer