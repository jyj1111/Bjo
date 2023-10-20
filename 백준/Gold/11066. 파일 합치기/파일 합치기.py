import sys
input=sys.stdin.readline


def MinCost(a,b):
    if a==b:
        return 0
    if b==a+1:
        return Files[a-1]+Files[a]
    if dp[a][b]!=-1:
        return dp[a][b]
    dp[a][b]=sys.maxsize
    for i in range(a,b):
        dp[a][b]=min(dp[a][b],MinCost(a,i)+MinCost(i+1,b)+hap[b]-hap[a-1])

    return dp[a][b]


for i in range(int(input())):
    K=int(input()) # 3 ≤ K ≤ 500
    Files=list(map(int,input().split()))
    hap=[0]*(K+1)
    
    for j in range(1,K+1):
        hap[j]=hap[j-1]+Files[j-1]
        
    dp=[[-1]*(K+1) for _ in range(K+1)]
    print(MinCost(1,K))