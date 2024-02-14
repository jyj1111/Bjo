import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**8)
n,m=map(int,input().split())

Maps=[list(input().rstrip('\n')) for _ in range(n)]
dp=[[0]*(m) for _ in range(n)]
dic={'U':[-1,0],'R':[0,1],'D':[1,0],'L':[0,-1]}

def DFS(y,x):
    if dp[y][x]:
        return
    
    dp[y][x]=1
    for dy,dx in dic.values():
        y1,x1=y+dy,x+dx
        if 0<=y1<n and 0<=x1<m:
            dy1,dx1=dic[Maps[y1][x1]]
            if dy+dy1==0 and dx+dx1==0:
                DFS(y1,x1)




Escapes=[]
for i in range(n):
    for j in range(m):
        if i==0 or i==n-1 or j==0 or j==m-1:
            di,dj=dic[Maps[i][j]]
            i1,j1=i+di,j+dj
            if i1<0 or i1>=n or j1<0 or j1>=m:
                Escapes.append((i,j))

for i,j in Escapes:
    DFS(i,j)

print(sum(sum(dp,[])))
        