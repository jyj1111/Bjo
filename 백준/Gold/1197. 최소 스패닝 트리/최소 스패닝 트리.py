import sys
input=sys.stdin.readline
def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,x,y):
    x=find_parent(parent,x)
    y=find_parent(parent,y)
    if x<y:
        parent[y]=x
    else:
        parent[x]=y
    
v,e=map(int,input().split())
parent=[0]*(v+1)
edges=[]
for i in range(1,v+1):
    parent[i]=i
for i in range(e):
    v1,v2,cost=map(int,input().split())
    edges.append((cost,v1,v2))

edges.sort()
res=0
for edge in edges:
    cost,a,b=edge
    if find_parent(parent,a)!=find_parent(parent,b):
        union_parent(parent,a,b)
        res+=cost

print(res)
