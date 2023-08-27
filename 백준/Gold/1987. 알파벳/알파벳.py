import sys
input=sys.stdin.readline
dic=set()
dy=[-1,0,1,0]
dx=[0,1,0,-1]
R,C=map(int,input().split()) ## R:세로, C:가로, 둘다 20이하
graph=[list(input().rstrip('\n')) for _ in range(R)]
dic.add(graph[0][0])
ans=1
def DFS(cnt,y,x):
    global ans
    ans=max(ans,cnt)
    for i in range(4):
        r1=y+dy[i]
        c1=x+dx[i]
        if 0<=r1<R and 0<=c1<C:
            if not graph[r1][c1] in dic:
                dic.add(graph[r1][c1])
                DFS(cnt+1,r1,c1)
                dic.remove(graph[r1][c1])
                
            

DFS(1,0,0)
print(ans)