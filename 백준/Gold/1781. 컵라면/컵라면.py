import sys
from heapq import heappush,heappop
input=sys.stdin.readline
n=int(input())
hw=[]
maxDay=0
for i in range(n):
    day,w=map(int,input().split())
    maxDay=max(maxDay,day)
    hw.append((day,w))

hw.sort()
pq=[]

for day,w in hw:
    if day<=len(pq):
        heappop(pq)
    heappush(pq,w)

print(sum(pq))