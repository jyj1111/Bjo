import sys
sys.setrecursionlimit(10**8)
from collections import defaultdict
input=sys.stdin.readline
n=int(input())
graph=defaultdict(list)

for i in range(n-1):
    n1,n2=map(int,input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

visited=[0]*(n+1)
dp=[[0]*(2) for _ in range(n+1)]

def DFS(parent):
    if visited[parent]:
        return
    visited[parent]=1
    dp[parent][0]=0
    dp[parent][1]=1
    for child in graph[parent]:
        if visited[child]:
            continue
        DFS(child)
        dp[parent][0]+=dp[child][1]
        dp[parent][1]+=min(dp[child][0],dp[child][1])

DFS(1)
print(min(dp[1][0],dp[1][1]))
        