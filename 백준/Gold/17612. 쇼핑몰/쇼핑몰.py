import sys
input=sys.stdin.readline
from heapq import heapify,heappush,heappop

n,k=map(int,input().split())
counters=[]
customers=[]

for i in range(1,n+1):
    Id,w=map(int,input().split())
    if len(counters)<k:
        heappush(counters,(w,i,Id))
    else:
        w1,counterId,customerId=heappop(counters)
        heappush(counters,(w+w1,counterId,Id))
        heappush(customers,(w1,-counterId,customerId))
        

while counters:
    w1,counterId,customerId=heappop(counters)
    heappush(customers,(w1,-counterId,customerId))

ans=0
for i in range(n):
    ans+=(i+1)*heappop(customers)[2]

print(ans)