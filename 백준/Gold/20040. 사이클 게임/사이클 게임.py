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

    
n,m=map(int,input().split()) # 3 ≤ n ≤ 500,000, 3 ≤ m ≤ 1,000,000
parent=[i for i in range(n)]
ans=0
for i in range(1,m+1):
    a,b=map(int,input().split())
    if Find(a)==Find(b):
        ans=i
        break
    Union(a,b)

print(ans)