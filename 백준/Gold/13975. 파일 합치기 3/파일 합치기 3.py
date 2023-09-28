import sys,heapq
input=sys.stdin.readline
t=int(input())
for i in range(t):
    k=int(input()) #3 ≤ K ≤ 1,000,000
    files=list(map(int,input().split()))
    heapq.heapify(files)
    cost=0
    while len(files)>1:
        #print(files)
        file1=heapq.heappop(files)
        file2=heapq.heappop(files)
        cost+=file1+file2
        heapq.heappush(files,file1+file2)
    print(cost)