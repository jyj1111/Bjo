import sys
input=sys.stdin.readline
INF=sys.maxsize
n,m=map(int,input().split())
dis=[[INF]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    dis[i][i]=0
for _ in range(m):
    s,e,flag=map(int,input().split())
    dis[s][e]=0
    dis[e][s]=(0 if flag else 1)


for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            dis[i][j]=min(dis[i][j],dis[i][k]+dis[k][j])

for _ in range(int(input())):
    s,e=map(int,input().split())
    print(dis[s][e])