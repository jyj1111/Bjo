import sys
input=sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
n,r,q=map(int,input().split())
counted=[0]*(n+1)
graph=[[] for i in range(n+1)]

for i in range(n-1):
    v1,v2=map(int,input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

def DFS(cur):
    counted[cur]=1
    for child in graph[cur]:
        if counted[child]==0:
            DFS(child)
            counted[cur]+=counted[child]
       
DFS(r)
for i in range(q):
    print(counted[int(input())])