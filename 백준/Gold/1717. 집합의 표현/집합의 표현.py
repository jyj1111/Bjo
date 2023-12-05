import sys
sys.setrecursionlimit(10**8)
input=sys.stdin.readline

n,m=map(int,input().split())

parents=[0]*(n+1)

def init():
    for i in range(n+1):
        parents[i]=i

def union(x,y):
    x=find(x)
    y=find(y)
    if x<y:
        parents[y]=x
    elif x>y:
        parents[x]=y
    else:
        return


def find(x):
    if x!=parents[x]:
        parents[x]=find(parents[x])
    return parents[x]


init()
for i in range(m):
    flag,a,b=map(int,input().split())
    if flag:
        if find(a)==find(b):
            print('YES')
        else:
            print('NO')

    else:
        union(a,b)
        #print(parents)