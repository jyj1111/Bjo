import sys
input=sys.stdin.readline
INF=sys.maxsize
n=int(input())
m=int(input())
graph=[[INF]*(n+1) for _ in range(n+1)]
path=[[-1]*(n+1) for _ in range(n+1)]

for i in range(m):
    y,x,w=map(int,input().split())
    graph[y][x]=min(graph[y][x],w)

for i in range(1,n+1):
    graph[i][i]=0
    

    
    
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if graph[i][j]>graph[i][k]+graph[k][j]:
                graph[i][j]=graph[i][k]+graph[k][j]
                path[i][j]=k
                
for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j]==INF:
            graph[i][j]=0
        
for i in range(1,n+1):
    print(*graph[i][1:])

def DFS(i,j):
    global minipath
    if path[i][j]==-1:
       minipath.append(i)
       minipath.append(j)
       return   
            
            
    else:
        DFS(i,path[i][j])
        minipath.append(path[i][j])
        DFS(path[i][j],j)
        
    

for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j]==0:
            print(0)
        else:
            minipath=[]
            DFS(i,j)
            minipath=list(dict.fromkeys(minipath))
            minipath.insert(0,len(minipath))
            print(*minipath)