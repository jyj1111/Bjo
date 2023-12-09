import sys,heapq
from heapq import heappush,heappop
from collections import deque
input=sys.stdin.readline

n,k=map(int,input().split())
jewels=[]
bags=[]

for i in range(n):
    m,v=map(int,input().split())
    jewels.append((m,v))
    

for i in range(k):
    bags.append(int(input()))
    
jewels.sort()
bags.sort()

jewels=deque(jewels)

maxHeap=[]
ans=0
for i in range(k):
    while jewels and bags[i]>=jewels[0][0]:
        heappush(maxHeap,-jewels[0][1])
        jewels.popleft()
    if maxHeap:
        ans-=heappop(maxHeap)

print(ans)
