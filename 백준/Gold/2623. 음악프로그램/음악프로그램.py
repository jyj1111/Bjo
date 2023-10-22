import sys
from collections import deque
input=sys.stdin.readline

"""
1->4->3
6->2->5->4
3->2
[1,1,1,1]
"""

N,M=map(int,input().split())# 1 ≤ N ≤ 1000, 1 ≤ M ≤ 100
graph=[[] for _ in range(N+1)]
degree=[0]*(N+1)
queue=deque()

for i in range(M):
    arr=list(map(int,input().split()))
    num=arr[0]
    arr1=arr[1:]
    for j in range(num-1):
        graph[arr1[j]].append(arr1[j+1])
        degree[arr1[j+1]]+=1
        

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

if len(ans)==N:
    for num in ans:
        print(num)
else:
    print(0)