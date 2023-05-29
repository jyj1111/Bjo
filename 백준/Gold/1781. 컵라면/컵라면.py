import sys
import heapq
input=sys.stdin.readline
n=int(input())
arr=[]
pq=[]
for i in range(n):
  day,profit=map(int,input().split())
  arr.append((day,profit))

arr.sort()

for i in range(n):
  heapq.heappush(pq,arr[i][1])
  if len(pq)>arr[i][0]:
    heapq.heappop(pq)

print(sum(pq))
  