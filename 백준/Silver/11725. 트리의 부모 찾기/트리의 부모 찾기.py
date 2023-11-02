import sys
input=sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
n=int(input())
visited=[0]*(n+1)
graph=[[] for i in range(n+1)]
res=[[] for i in range(n+1)]
for i in range(n-1):
    v1,v2=map(int,input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

def DFS(parent):
    visited[parent]=1
    for child in graph[parent]:
        if visited[child]==0:
            res[child].append(parent)
            DFS(child)
        
DFS(1)

for i in range(2,len(res)):
    print(*res[i])