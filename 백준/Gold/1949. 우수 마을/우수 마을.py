import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**8)
N=int(input())#N<=10000
townPeoples=list(map(int,input().split()))
graph=[[] for _ in range(N+1)]
visited=[0]*(N+1)
dp=[[0,0] for _ in range(N+1)]
townPeoples.insert(0,0)

def DFS(root):
    #print(root)
    #print(dp)
    if visited[root]:
        return
    visited[root]=1
    dp[root][0]=0 # 일반마을
    dp[root][1]=townPeoples[root]# 우수마을
    for child in graph[root]:
        if visited[child]:
            continue
        
        DFS(child)
        dp[root][0]+=max(dp[child][0],dp[child][1])
        dp[root][1]+=dp[child][0]
            
    

for i in range(1,N):
    town1,town2=map(int,input().split())
    graph[town1].append(town2)
    graph[town2].append(town1)

DFS(1)
#print(dp)
print(max(dp[1][0],dp[1][1]))