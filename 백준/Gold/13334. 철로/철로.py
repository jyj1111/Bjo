import sys
input=sys.stdin.readline
##from collections import deque
from heapq import heappush,heappop

n=int(input())

arr=[]
for i in range(n):
    start,end=map(int,input().split())
    if start>end:
        start,end=end,start
    arr.append((start,end))
arr.sort(key=lambda x:x[1])

minHeap=[]

d=int(input())

ans=0
for i in range(n):
    start,end=arr[i]
    if end-start>d:
        continue        
    heappush(minHeap,start)
    while end-minHeap[0]>d:
        heappop(minHeap)
    ans=max(ans,len(minHeap))   
    
print(ans)    