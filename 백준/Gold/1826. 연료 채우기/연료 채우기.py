import sys
from heapq import heappush,heappop
input=sys.stdin.readline

N=int(input())
arr=[]

for i in range(N):
    dis,fuel=map(int,input().split())
    arr.append([dis,fuel])
    
L,P=map(int,input().split())
maxDis=P
maxHeap=[]

arr.append([L,0])
arr.sort(key=lambda x:x[0])


idx=0
cnt=0
while idx<N+1:
    dis,fuel=arr[idx]
    #print(dis,fuel)
    if maxDis<dis:
        if maxHeap:
            cnt+=1
            maxDis+=-heappop(maxHeap)
        else:
            break        
    else:
        heappush(maxHeap,-fuel)
        idx+=1
    

if maxDis<L:
    print(-1)
else:
    print(cnt)