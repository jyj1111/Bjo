import sys
input=sys.stdin.readline
MAX=sys.maxsize
from heapq import heappush,heappop
t=int(input())

def dijkstra(i,x,y):
    global dis
    pq=[]
    heappush(pq,(0,x,y))
    dis[i][x][y]=0
    while pq:
        wei,x1,y1=heappop(pq)
        #print(w,x1,y1)
        if dis[i][x1][y1]<wei:
            continue
        for dx,dy in [(-1,0),(0,1),(1,0),(0,-1)]:
            x2=x1+dx
            y2=y1+dy
            if 0<=x2<h+2 and 0<=y2<w+2:
                if graph[x2][y2]=='*':
                    continue
                elif graph[x2][y2]=='.':
                    if wei<dis[i][x2][y2]:
                        dis[i][x2][y2]=wei
                        heappush(pq, (wei,x2,y2))                    

                elif graph[x2][y2]=='#':
                    if wei+1<dis[i][x2][y2]:
                        dis[i][x2][y2]=wei+1
                        heappush(pq, (wei+1,x2,y2))
    
                    

for i in range(t):
    h,w=map(int,input().split())
    graph=[['.']*(w+2)]+[list('.'+input().rstrip('\n')+'.') for _ in range(h)]+[['.']*(w+2)]
    persons=[(0,0)]
    for x in range(h+2):
        for y in range(w+2):
            if graph[x][y]=='$':
                graph[x][y]='.'
                persons.append((x,y))
                

    dis=[[[MAX]*(w+2) for _ in range(h+2)] for _ in range(3)]
    for idx,point in enumerate(persons):
         x,y=point
         dijkstra(idx,x,y)
         
    ans=MAX
    for x in range(h+2):
         for y in range(w+2):
             hap=dis[0][x][y]+dis[1][x][y]+dis[2][x][y]
             if graph[x][y]=='.':
                 ans=min(ans,hap)

             elif graph[x][y]=='#':
                 ans=min(ans,hap-2)
                 
    print(ans)