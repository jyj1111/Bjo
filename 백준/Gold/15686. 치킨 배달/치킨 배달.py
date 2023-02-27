import sys
input=sys.stdin.readline
from itertools import combinations
INF=sys.maxsize
n,m=map(int,input().split())
graph=[]
for i in range(n):
    arr=list(map(int,input().split()))
    graph.append(arr)

home=[]
chicken=[]

for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            home.append([i+1,j+1])
        elif graph[i][j]==2:
            chicken.append([i+1,j+1])

totalDistance=INF
chickenCombination=[]
for j in range(1,m+1):
    for combi in list(combinations(chicken,j)):
        chickenCombination.append(combi)

for combi in chickenCombination:
    distancehap=0;
    for x1,y1 in home:
        distance=INF
        for x2,y2 in combi:
            distance=min(distance,abs(x1-x2)+abs(y1-y2))
            
        distancehap+=distance
        
    totalDistance=min(totalDistance,distancehap) 
    
print(totalDistance)       