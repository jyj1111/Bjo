import sys
input=sys.stdin.readline
n=int(input())
k=int(input())

dp=[[0]*(1001) for _ in range(1001)]

for i in range(1,1001):
    dp[i][0]=1
    dp[i][1]=i

for i in range(2,n):
    for j in range(2,k+1):
        dp[i][j]=(dp[i-2][j-1]+dp[i-1][j])%1000000003 
            

print((dp[n-3][k-1]+dp[n-1][k])%1000000003)