import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)
n,m=map(int,input().split())


dp=[[0]*(m) for _ in range(n)]
visited=[[0]*(m) for _ in range(n)]
graph=[list(input().rstrip('\n')) for _ in range(n)]


def DFS(i,j):
    #print(i,j)
    if 0>i or 0>j or i>=n or j>=m:
        return 0
    if graph[i][j]=='H':
        return 0
    if visited[i][j]:
        print(-1)
        sys.exit(0)
        
    if dp[i][j]:
        return dp[i][j]

    visited[i][j]=1
    for di,dj in [(-1,0),(0,1),(1,0),(0,-1)]:
        k=int(graph[i][j])
        i1=i+(k*di)
        j1=j+(k*dj)
        dp[i][j]=max(dp[i][j],1+DFS(i1,j1))
                
    visited[i][j]=0
    return dp[i][j]

print(DFS(0,0))