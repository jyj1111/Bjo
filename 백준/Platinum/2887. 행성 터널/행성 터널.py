import sys
input=sys.stdin.readline


def find(x):
    if parents[x]!=x:
        parents[x]=find(parents[x])
    return parents[x]

def union(a,b):
    a=find(a)
    b=find(b)
    if a<b:
        parents[b]=a
    else:
        parents[a]=b

n=int(input())
parents=[i for i in range(n+1)]
pointXs=[]
pointYs=[]
pointZs=[]
edges=[]

for i in range(1,n+1):
    x,y,z=map(int,input().split())
    pointXs.append((x,i))
    pointYs.append((y,i))
    pointZs.append((z,i))
pointXs.sort()
pointYs.sort()
pointZs.sort()
points=[pointXs,pointYs,pointZs]

for i in range(3):
    for j in range(n-1):
        k1,j1=points[i][j]
        k2,j2=points[i][j+1]
        edges.append((abs(k1-k2),j1,j2))
    

edges.sort()
ans=0
for cost,i,j in edges:
    #print(i,j,cost)
    #print(parents)
    if find(i)==find(j):
        continue
    union(i,j)
    ans+=cost
    

print(ans)