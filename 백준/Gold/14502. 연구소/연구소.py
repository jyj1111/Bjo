import sys
input=sys.stdin.readline
from itertools import combinations
import copy
from collections import deque
dx=[1,0,-1,0]
dy=[0,1,0,-1]
n,m=map(int,input().split())
graph=[]
for i in range(n):
    arr=list(map(int,input().split()))
    graph.append(arr)

protect=[]
virus=[]
safe=[]
for i in range(n):
    for j in range(m):
        if graph[i][j]==1:
            protect.append([i,j])
        elif graph[i][j]==2:
            virus.append([i,j])
        else:
            safe.append([i,j])
            
answer=0;
for combi in list(combinations(safe,3)):
    copyGraph=copy.deepcopy(graph)
    for y,x in combi:
        copyGraph[y][x]=1
    for y1,x1 in virus:
        queue=deque()
        queue.append([y1,x1])
        while queue:
            visited=queue.popleft()
            for i in range(4):
                x=visited[1]+dx[i]
                y=visited[0]+dy[i]
                if 0<=x and x<m and 0<=y and y<n and copyGraph[y][x]==0:
                        copyGraph[y][x]=2
                        queue.append([y,x])
                  
    cnt=0
    for i in range(n):
        for j in range(m):
            if copyGraph[i][j]==0:
                cnt+=1
    answer=max(answer,cnt)
    
print(answer)