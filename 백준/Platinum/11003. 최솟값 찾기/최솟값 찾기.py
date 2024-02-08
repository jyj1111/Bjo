import sys
from collections import deque

input=sys.stdin.readline
n,l=map(int,input().split())
arr=list(map(int,input().split()))

queue=deque()
ans=[]

for i in range(n):

    while queue and queue[0]+l==i:
        queue.popleft()
    while queue and arr[queue[-1]]>arr[i]:
        queue.pop()

    queue.append(i)
    ans.append(arr[queue[0]])

print(*ans)
    