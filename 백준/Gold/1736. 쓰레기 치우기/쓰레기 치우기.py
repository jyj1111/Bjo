import sys
input=sys.stdin.readline
n,m=map(int,input().split())
maps=[list(map(int,input().split())) for _ in range(n)]

cnt=0
for i in range(n):
    for j in range(m):
        if maps[i][j]:
            cnt+=1

ans=0
while cnt:
    start=0
    for i in range(n):
        tmp=start
        for j in range(tmp,m):
            if maps[i][j]:
                maps[i][j]=0
                cnt-=1
                start=j
               
    ans+=1

print(ans)