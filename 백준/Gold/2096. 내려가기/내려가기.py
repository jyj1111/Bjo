import sys
input=sys.stdin.readline

n=int(input())# n<=100000
dp=[[[0,0] for _ in range(3)] for _ in range(2)]

for i in range(1,n+1):
    left,mid,right=map(int,input().split())
    dp[1][0][0]= max(dp[0][0][0],dp[0][1][0])+left
    dp[1][1][0]= max(dp[0][0][0],dp[0][1][0],dp[0][2][0])+mid
    dp[1][2][0]= max(dp[0][1][0],dp[0][2][0])+right
    dp[1][0][1]= min(dp[0][0][1],dp[0][1][1])+left
    dp[1][1][1]= min(dp[0][0][1],dp[0][1][1],dp[0][2][1])+mid
    dp[1][2][1]= min(dp[0][1][1],dp[0][2][1])+right
    dp[0][0][0]= dp[1][0][0]
    dp[0][1][0]= dp[1][1][0]
    dp[0][2][0]= dp[1][2][0]
    dp[0][0][1]= dp[1][0][1]
    dp[0][1][1]= dp[1][1][1]
    dp[0][2][1]= dp[1][2][1]



print(max(dp[1][0][0],dp[1][1][0],dp[1][2][0]),min(dp[1][0][1],dp[1][1][1],dp[1][2][1]))

