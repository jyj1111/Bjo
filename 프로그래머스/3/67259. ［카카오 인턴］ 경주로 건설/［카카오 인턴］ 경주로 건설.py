from collections import deque
import math
dy=[-1,0,1,0]
dx=[0,1,0,-1]
def BFS(board):
    queue=deque([])
    n=len(board)
    queue.append([0,0,0,0])
    minCost=math.inf
    dp=[[[minCost]*(3) for _ in range(n)] for _ in range(n)]
    dp[0][0][0]=0
    while queue:
        y,x,dir1,cost=queue.popleft()
        #print(y,x,cost)
        dir2=0
        for k in range(4):
            y1=y+dy[k]
            x1=x+dx[k]
            if y1-y!=0:
                dir2=1                                    
            elif x1-x!=0:
                dir2=2
            if 0<=y1<n and 0<=x1<n and board[y1][x1]==0:
                if dir1!=dir2:
                    if dir1==0 and dp[y1][x1][dir2]>cost+100:
                        dp[y1][x1][dir2]=cost+100
                        queue.append([y1,x1,dir2,cost+100])
                    elif dir1!=0 and dp[y1][x1][dir2]>cost+100:
                        dp[y1][x1][dir2]=cost+600
                        queue.append([y1,x1,dir2,cost+600])
                elif dir1==dir2 and dp[y1][x1][dir2]>cost+100:
                    dp[y1][x1][dir2]=cost+100
                    queue.append([y1,x1,dir2,cost+100])
                   
    return min(dp[n-1][n-1][1],dp[n-1][n-1][2])
                    
       

def solution(board):
    answer = BFS(board)
    return answer