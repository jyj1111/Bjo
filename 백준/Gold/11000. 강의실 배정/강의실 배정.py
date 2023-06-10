import sys
input=sys.stdin.readline
import heapq
n=int(input())
lectureTimes=[]

for i in range(n):
    s,t=map(int,input().split())
    lectureTimes.append([s,t])
    
lectureTimes.sort(key=lambda x:x[0])
endTime=[]
heapq.heappush(endTime,lectureTimes[0][1])
for i in range(1,n):
    if endTime[0]<=lectureTimes[i][0]:
        heapq.heappop(endTime)
    heapq.heappush(endTime,lectureTimes[i][1])    
   
        
        
    

print(len(endTime))