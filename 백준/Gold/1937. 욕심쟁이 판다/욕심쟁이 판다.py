import sys
input=sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
n=int(input())

graph=[list(map(int,input().split())) for _ in range(n)]
dp=[[0]*(n) for _ in range(n)]

dy=[-1,0,1,0]
dx=[0,1,0,-1]

ans=0

def dfs(i,j):
    if dp[i][j]:
        return dp[i][j]
    ##print(dp)
    dp[i][j]=1
    for k in range(4):
        y1=i+dy[k]
        x1=j+dx[k]
        if 0<=y1<n and 0<=x1<n and graph[y1][x1]>graph[i][j]:
            dp[i][j]=max(dp[i][j],dfs(y1,x1)+1)

    return dp[i][j]
    

for i in range(n):
    for j in range(n):
        ans=max(ans,dfs(i,j))
 
                
       

print(ans)