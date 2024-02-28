import sys
input=sys.stdin.readline
from heapq import heappush,heappop

n,k=map(int,input().split())
counterIn=[]
counterOut=[]


for i in range(n):
    pid,w=map(int,input().split())
    if len(counterIn)<k:
        heappush(counterIn,(w,i,pid))
        
    else:
        w1,cid,pid1=heappop(counterIn)
        heappush(counterIn,(w+w1,cid,pid))
        heappush(counterOut,(w1,-cid,pid1))

while counterIn:
    w1,cid,pid1=heappop(counterIn)
    heappush(counterOut,(w1,-cid,pid1))

answer=0
idx=0
while counterOut:
    idx+=1
    w,cid,pid=heappop(counterOut)
    answer+=idx*pid
    

print(answer)