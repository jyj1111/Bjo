import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**8)
n=int(input())#n<=10000
graph=[[] for _ in range(n+1)]


def DFS(root):

    if visited[root]:
        return
    visited[root]=1
    for neighbor,w in graph[root]:
        if visited[neighbor]:
            continue
        rootDis[neighbor]=rootDis[root]+w 
        DFS(neighbor)
        

for i in range(1,n):
    u,v,w=map(int,input().split())
    graph[u].append((v,w))
    graph[v].append((u,w))

visited=[0]*(n+1)
rootDis=[0]*(n+1)
DFS(1)

rootMax=0
idx=1
for i in range(1,n+1):
    if rootDis[i]>=rootMax:
        idx=i
        rootMax=rootDis[i]

visited=[0]*(n+1)
rootDis=[0]*(n+1)
DFS(idx)

print(max(rootDis))