import sys
input=sys.stdin.readline
MAX=sys.maxsize
cost,n=map(int,input().split())

arr=[]

dp=[MAX]*(1101)
dp[0]=0

for i in range(n):
    invest,people=map(int,input().split())
    arr.append((invest,people))

for i in range(1,1101):
    for cost1,people in arr:
        if i>=people:
            dp[i]=min(dp[i],dp[i-people]+cost1)

for i in range(1,1101):
    tmp=dp[i]
    for j in range(i+1,1101):
        tmp=min(tmp,dp[j])
        
    dp[i]=tmp

print(dp[cost])