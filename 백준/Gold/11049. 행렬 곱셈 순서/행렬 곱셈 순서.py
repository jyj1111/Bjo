import sys
input=sys.stdin.readline

"""

"""

N=int(input()) # 1 ≤ N ≤ 500
Matrixes=[list(map(int,input().split())) for _ in range(N)]

dp=[[-1]*(N) for _ in range(N)]

def MinMultiple(a,b):
    if a==b:
        return 0
    if dp[a][b]!=-1:
        return dp[a][b]
    dp[a][b]=sys.maxsize
    for i in range(a,b):
        dp[a][b]=min(dp[a][b],MinMultiple(a,i)+MinMultiple(i+1,b)+Matrixes[a][0]*Matrixes[i][1]*Matrixes[b][1])
    return dp[a][b]
    

print(MinMultiple(0,N-1))