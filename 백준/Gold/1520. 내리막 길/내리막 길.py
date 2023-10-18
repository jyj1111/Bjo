import sys
sys.setrecursionlimit(10 ** 9)
input=sys.stdin.readline

M,N=map(int,input().split())
boards=[list(map(int,input().split())) for _ in range(M)]
dp=[[-1]*(N) for _ in range(M)]
di=[-1,0,1,0]
dj=[0,1,0,-1]

def DFS(i,j):

    if i==M-1 and j==N-1:
        return 1
    
    if dp[i][j]==-1:
        dp[i][j]=0
        for k in range(4):
            i1=di[k]+i
            j1=dj[k]+j
            if 0<=i1<M and 0<=j1<N and boards[i1][j1]<boards[i][j]:
                dp[i][j]+=DFS(i1,j1)
    return dp[i][j]


print(DFS(0,0))