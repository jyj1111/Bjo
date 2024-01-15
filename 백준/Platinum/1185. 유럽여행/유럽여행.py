import sys
input=sys.stdin.readline
n,k=map(int,input().split())
costs=[0]

parents=[0]*(n+1)

def init():
    for i in range(1,n+1):
        parents[i]=i

def find(n1):
    if parents[n1]==n1:
        return n1
    else:
        parents[n1]=find(parents[n1])
    return parents[n1]


def union(n1,n2):
    n1=find(n1)
    n2=find(n2)
    if n1<n2:
        parents[n2]=n1
    else:
        parents[n1]=n2


ans=1001

for i in range(n):
    cost=int(input())
    ans=min(ans,cost)
    costs.append(cost)

graph=[]
for i in range(k):
    n1,n2,w=map(int,input().split())
    if n1>n2:
        n1,n2=n2,n1
    cost=costs[n1]+costs[n2]+2*(w)
    graph.append((cost,n1,n2))

graph.sort(key=lambda x:x[0])
init()
for cost,n1,n2 in graph:
    if find(n1)!=find(n2):
        union(n1,n2)
        ans+=cost

print(ans)
    