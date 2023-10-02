import sys
input=sys.stdin.readline
from collections import deque
N,K=map(int,input().split()) #0 ≤ N, K ≤ 100,000

visited=[0]*(100001)

def BFS(N):
    global visited
    queue=deque()
    queue.append(N)
    visited[N]=1
    while queue:
        x=queue.popleft()
        
        if x==K:
            break
        else:
            for k in [2*x,x-1,x+1]:
                if k<0 or k>100000:
                    continue
                if visited[k]:
                    continue
                if k==2*x:
                    queue.append(k)
                    visited[k]=visited[x]

                else:
                    queue.append(k)
                    visited[k]=visited[x]+1
    
                  
BFS(N)
print(visited[K]-1)