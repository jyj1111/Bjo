import sys
input=sys.stdin.readline
INF=sys.maxsize
n=int(input())
RGB=[list(map(int,input().split())) for _ in range(n)]
ans=INF

for j in range(3):
    dp=[[0,0,0] for _ in range(n+1)]
    dp[1][j]=INF
    for k in range(3):
        if k!=j:
            dp[1][k]=RGB[0][k]
    for i in range(2,n+1):
        dp[i][0]=min(dp[i-1][1],dp[i-1][2])+RGB[i-1][0]
        dp[i][1]=min(dp[i-1][0],dp[i-1][2])+RGB[i-1][1]
        dp[i][2]=min(dp[i-1][0],dp[i-1][1])+RGB[i-1][2]
    ans=min(ans,dp[n][j])

print(ans)