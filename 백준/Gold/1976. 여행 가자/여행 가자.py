import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)


def Union(a,b):
    a=Find(a)
    b=Find(b)
    if a>b:
        parent[a]=b
    else:
        parent[b]=a

def Find(x):
    if x!=parent[x]:
        parent[x]=Find(parent[x])
    return parent[x]

    
N=int(input())# N<=200
M=int(input())# M<=1000
graph=[[]for _ in range(N+1)]
parent=[i for i in range(N+1)]

for i in range(N):
    info=list(map(int,input().split()))
    for j in range(N):
        if info[j]==1:
            graph[i+1].append(j+1)
            Union(i+1,j+1)

plans=list(map(int,input().split()))
plans=set([parent[plan] for plan in plans])

if len(plans)==1:
    print('YES')
else:
    print('NO')
