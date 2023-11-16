import sys,heapq
input=sys.stdin.readline
N=int(input())

Meetings=[]
for i in range(N):
    start,end=map(int,input().split())
    Meetings.append((start,end))

Meetings.sort(key=lambda x:x[0])

pq=[]
heapq.heapify(pq)
heapq.heappush(pq,Meetings[0][1])

for i in range(1,N):
    if Meetings[i][0]>=pq[0]:
        heapq.heappop(pq)
        
    heapq.heappush(pq,Meetings[i][1])

print(len(pq))
    
    