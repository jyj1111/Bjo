import sys
input=sys.stdin.readline
from collections import defaultdict

n,m=map(int,input().split())

jumpXs=defaultdict(int)

for i in range(m):
    jumpXs[int(input())]=1    


dp=[[10000]*(int((2*n)**0.5)+2) for _ in range(n+1)]


dp[1][0]=0

for i in range(2,n+1):
    if i in jumpXs:
        continue
    for v in range(1,int((2*i)**0.5)+1):
            dp[i][v]=min(dp[i-v][v-1],dp[i-v][v],dp[i-v][v+1])+1


ans=min(dp[n])
print(-1 if ans==10000 else ans)