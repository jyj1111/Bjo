import sys
input=sys.stdin.readline
MAX=sys.maxsize

n=int(input())
costs=[list(map(int,input().split())) for _ in range(n)]

dp=[[MAX]*(1<<n) for _ in range(n+1)]

dp[0][0]=0
for i in range(1,n+1):
    for j in range(1<<n):
        if dp[i-1][j]==MAX:
            continue
        for k in range(n):
            if j&(1<<k):
                continue
            dp[i][j|(1<<k)]=min(dp[i][j|(1<<k)],dp[i-1][j]+costs[i-1][k])

print(dp[n][(1<<n)-1])
