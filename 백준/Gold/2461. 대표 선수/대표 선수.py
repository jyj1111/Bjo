import sys,heapq
input=sys.stdin.readline

N,M=map(int,input().split())#1<N,M<1000
students=[sorted(list(map(int,input().split()))) for _ in range(N)]
ans=sys.maxsize


maxPointer=0
pointers=[0]*(N)
arr=[students[i][pointers[i]] for i in range(N)]
mx=max(arr)
minHeap=[]

for i in range(N):
    heapq.heappush(minHeap,(arr[i],i))
    

while True:
    mn,i=heapq.heappop(minHeap)
    ans=min(ans,mx-mn)    
    pointers[i]+=1
    maxPointer=pointers[i]
    if maxPointer==M:
        break
    arr[i]=students[i][pointers[i]]
    heapq.heappush(minHeap,(arr[i],i))
    mx=max(mx,arr[i])
    
    
    
    
print(ans)