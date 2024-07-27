import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**8)

r,c=map(int,input().split())
graph=[list(input().rstrip('\n')) for _ in range(r)]
ans=0

def DFS(y,x):
    #print(y,x)
    if x==0:
        return True

    for dy,dx in [(-1,-1),(0,-1),(1,-1)]:
        y1,x1=y+dy,x+dx
        if 0<=y1<r and 0<=x1<c and graph[y1][x1]=='.':
            graph[y1][x1]='x'
            if DFS(y1,x1):
                return True
            
    return False
            


for y in range(r):
    ans+=int(DFS(y,c-1))

print(ans)
    