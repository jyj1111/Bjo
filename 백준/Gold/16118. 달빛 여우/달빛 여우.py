import sys
from collections import defaultdict
from heapq import heappop,heappush

MAX=sys.maxsize
input=sys.stdin.readline
n,e=map(int,input().split())
graph=[[] for _ in range(n+1)]

for i in range(e):
    n1,n2,w=map(int,input().split())
    graph[n1].append((n2,w))
    graph[n2].append((n1,w))
    
foxDis=[MAX]*(n+1)
foxDis[1]=0
pq=[]
heappush(pq,(0,1))

while pq:
    w,cur=heappop(pq)
    if foxDis[cur]<w:
        continue

    for neighbor,w1 in graph[cur]:
        if foxDis[neighbor]>w+w1:
            foxDis[neighbor]=w+w1
            heappush(pq,(w+w1,neighbor))


wolfDis=[[MAX]*(2) for _ in range(n+1)]
wolfDis[1][0]=0
pq1=[]
heappush(pq1,(0,1,0))

while pq1:
    w,cur,cnt=heappop(pq1)
    if wolfDis[cur][cnt]<w:
        continue

    for neighbor,w1 in graph[cur]:
        cnt1=(cnt+1)%2
        if cnt1%2==1:
            if wolfDis[neighbor][cnt1]>w+(0.5*w1):
                wolfDis[neighbor][cnt1]=w+(0.5*w1)
                heappush(pq1,(w+(0.5*w1),neighbor,cnt1))

        else:
            if wolfDis[neighbor][cnt1]>w+(2*w1):
                wolfDis[neighbor][cnt1]=w+(2*w1)
                heappush(pq1,(w+(2*w1),neighbor,cnt1))


ans=0

for i in range(2,n+1):
    if foxDis[i]<min(wolfDis[i][0],wolfDis[i][1]):
        ans+=1

print(ans)