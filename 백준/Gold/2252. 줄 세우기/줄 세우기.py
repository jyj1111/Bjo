import sys
from collections import deque
input=sys.stdin.readline

"""
4->2
3->1
"""

N,M=map(int,input().split())# 1 ≤ N ≤ 32,000, 1 ≤ M ≤ 100,000
graph=[[] for _ in range(N+1)]
degree=[0]*(N+1)
queue=deque()
for i in range(M):
    s1,s2=map(int,input().split())
    graph[s1].append(s2)
    degree[s2]+=1

for i in range(1,N+1):
    if degree[i]==0:
        queue.append(i)

ans=[]
while queue:
    n=queue.popleft()
    ans.append(n)
    for j in graph[n]:
        degree[j]-=1
        if degree[j]==0:
            queue.append(j)
        

print(*ans)