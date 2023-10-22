import sys
import heapq
input=sys.stdin.readline

"""
4(0)->2(1)
3(0)->1(1)
"""

N,M=map(int,input().split())# 1 ≤ N ≤ 32,000, 1 ≤ M ≤ 100,000
graph=[[] for _ in range(N+1)]
degree=[0]*(N+1)
pq=[]
heapq.heapify(pq)
for i in range(M):
    s1,s2=map(int,input().split())
    graph[s1].append(s2)
    degree[s2]+=1

for i in range(1,N+1):
    if degree[i]==0:
        heapq.heappush(pq,i)

ans=[]
while pq:
    n=heapq.heappop(pq)
    ans.append(n)
    for j in graph[n]:
        degree[j]-=1
        if degree[j]==0:
            heapq.heappush(pq,j)
        

print(*ans)