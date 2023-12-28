import sys
input=sys.stdin.readline

n,m=map(int,input().split())

dp=[[0]*(m+1) for _ in range(n+1)]
path=[[0]*(m+1) for _ in range(n+1)]
arr=[[0]*(m+1)]

for i in range(n):
    arr.append(list(map(int,input().split())))

for i in range(1,n+1):
    for j in range(1,m+1):
        for w in range(i+1):
            v=arr[w][j]
            if dp[i][j]<dp[i-w][j-1]+v:
                dp[i][j]=dp[i-w][j-1]+v
                path[i][j]=w
                
                
                
                    

cur=m
cost=n
ans=[]
while cur>0:
    ans.append(path[cost][cur])
    cost-=path[cost][cur]
    cur-=1
    
ans.reverse()
print(dp[n][m])
print(*ans)
                