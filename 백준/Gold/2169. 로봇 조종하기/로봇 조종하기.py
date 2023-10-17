import sys,copy
input=sys.stdin.readline

N,M=map(int,input().split())#1≤N, M≤1,000
dp=[list(map(int,input().split())) for _ in range(N)]


for j in range(1,M):
    dp[0][j]+=dp[0][j-1]

for i in range(1,N):
    LtoR=copy.deepcopy(dp[i])
    RtoL=copy.deepcopy(dp[i])

    for j in range(M):
        if j==0:
             LtoR[j]+=dp[i-1][j]

        else:
            LtoR[j]+=max(dp[i-1][j],LtoR[j-1])

    for j in range(M-1,-1,-1):
        if j==M-1:
             RtoL[j]+=dp[i-1][j]

        else:
            RtoL[j]+=max(dp[i-1][j],RtoL[j+1])
    
            
    for j in range(M):
        dp[i][j]=max(LtoR[j],RtoL[j])

print(dp[N-1][M-1])