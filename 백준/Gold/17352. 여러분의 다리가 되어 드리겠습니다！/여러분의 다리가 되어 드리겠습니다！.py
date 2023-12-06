import sys
sys.setrecursionlimit(10**8)
input=sys.stdin.readline

def find(x):
    if parents[x]!=x:
        parents[x]=find(parents[x])
    return parents[x]

def union(x,y):
    x=find(x)
    y=find(y)
    if x<y:
        parents[y]=x
    elif x>y:
        parents[x]=y
    else:
        return
    
def init():
    for i in range(n+1):
        parents[i]=i

        
n=int(input())

parents=[0]*(n+1)
init()


for i in range(n-2):
    n1,n2=map(int,input().split())
    union(find(n1),find(n2))

ans=[1,1]

for i in range(1,n+1):
    if find(i)!=1:
        ans[1]=i
        break
        
print(*ans)