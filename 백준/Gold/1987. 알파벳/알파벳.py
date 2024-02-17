import sys
input=sys.stdin.readline
n,m=map(int,input().split())

Maps=[list(input().rstrip('\n')) for _ in range(n)]
visited=[0]*(26)

ans=0

def DFS(y,x,cnt):
    global ans
    ans=max(ans,cnt)
    for dy,dx in [(1,0),(-1,0),(0,1),(0,-1)]:
        y1,x1=y+dy,x+dx
        if 0<=y1<n and 0<=x1<m and visited[ord(Maps[y1][x1])-65]==0:
            n1=ord(Maps[y1][x1])-65
            visited[n1]=1
            DFS(y1,x1,cnt+1)
            visited[n1]=0

visited[ord(Maps[0][0])-65]=1
DFS(0,0,1)
print(ans)