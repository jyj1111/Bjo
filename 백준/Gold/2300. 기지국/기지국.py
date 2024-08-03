import sys
input=sys.stdin.readline
n=int(input())

arr=[(-1000001,1000001)]

for _ in range(n):
    x,y=map(int,input().split())
    arr.append((x,abs(y)))
    
arr.sort()

dp=[2000000]*(n+1)
dp[0]=0

for i in range(1,n+1):
    y=0
    for j in range(i,0,-1):
        y=max(y,arr[j][1])
        dp[i]=min(dp[i],dp[j-1]+max(arr[i][0]-arr[j][0],2*y))


print(dp[n])