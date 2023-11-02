import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**8)
N=int(input())#N<=1000000
graph=[[] for _ in range(N+1)]
visited=[0]*(N+1)
dp=[[0,0] for _ in range(N+1)]

def DFS(root):
    #print(root)
    #print(dp)
    if visited[root]:
        return
    visited[root]=1
    dp[root][0]=0 # earlyAdaptor X
    dp[root][1]=1# earlyAdaptor O
    for child in graph[root]:
        if visited[child]:
            continue
        
        DFS(child)
        dp[root][0]+=dp[child][1]
        dp[root][1]+=min(dp[child][0],dp[child][1])
            
    

for i in range(1,N):
    u,v=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

DFS(1)
#print(dp)
print(min(dp[1][0],dp[1][1]))