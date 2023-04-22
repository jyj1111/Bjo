import sys
import math
input=sys.stdin.readline

n=int(input())
dp=[i for i in range(0,n+1)]

for i in range(1,n+1):
    for j in range(1,math.floor(i**0.5)+1):
        if dp[i]>dp[i-j**2]+1:
            dp[i]=dp[i-j**2]+1

print(dp[n])
        