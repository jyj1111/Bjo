import sys
sys.setrecursionlimit(10**8)
input=sys.stdin.readline

n=int(input())
e=int(input())
parents=[0]*(n+1)

def init():
    for i in range(n+1):
        parents[i]=i

def find(a):
    if parents[a]==a:
        return a
    parents[a]=find(parents[a])
    return parents[a] 
   

def union(a,b):
    a=find(a)
    b=find(b)
    if a==b:
        return

    for i in range(a,b+1):
        if parents[i]!=a:
            parents[i]=a



init()
arr=[]
for i in range(e):
    start,end=map(int,input().split())
    if start>end:
        start,end=end,start
    arr.append((start,end))

arr.sort(key=lambda x:(x[0],x[1]))

small,large=0,0

for start,end in arr:
    if start<=large and end>large:
        large=end
    elif start>large:
        union(small,large)
        small=start
        large=end
        
union(small,large)    

print(len(set(parents))-1)