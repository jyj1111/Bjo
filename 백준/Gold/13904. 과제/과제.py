import sys,heapq
input=sys.stdin.readline


pq=[]
heapq.heapify(pq)

N=int(input())#N<1000

maxDay=0
for i in range(N):
    dday,point=map(int,input().split())#dday<=1000, point<=100
    heapq.heappush(pq,(-point,dday))
    maxDay=max(maxDay,dday)

assigned=[0]*(maxDay+1)
while pq:
    point,dday=heapq.heappop(pq)
    point=-point
    for day in range(dday,0,-1):
        if assigned[day]:
            continue
        assigned[day]=point
        break

print(sum(assigned))