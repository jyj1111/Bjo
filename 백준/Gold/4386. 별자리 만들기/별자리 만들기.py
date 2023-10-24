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
points=[[0,0]]
edges=[]
parents=[i for i in range(n+1)]
for i in range(n):
    x,y=map(float,input().split())
    points.append([x,y])

for i in range(1,n+1):
    for j in range(i+1,n+1):
        dis=(((points[j][0]-points[i][0])**2)+((points[j][1]-points[i][1])**2))**0.5
        #print(i,j)
        edges.append([i,j,dis])
        

edges.sort(key=lambda x:x[2])
ans=0
for i,j,cost in edges:
    #print(i,j)
    if find(i)==find(j):
        continue
    union(i,j)
    ans+=cost

print(round(ans,2))