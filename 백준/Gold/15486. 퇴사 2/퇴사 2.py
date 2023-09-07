import sys
input=sys.stdin.readline
n=int(input())
dp=[0]*(n+2)

for i in range(1,n+1):
    t,p=map(int,input().split())
    if dp[i+1]<dp[i]:
        dp[i+1]=dp[i]
    if i+t>n+1:
        continue
    else:
         dp[i+t]=max(dp[i]+p,dp[i+t])
         
                
print(dp[n+1])
        