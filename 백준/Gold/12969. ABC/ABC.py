import sys
input=sys.stdin.readline
from collections import defaultdict
n,k=map(int,input().split())

MAX=n+1
MAXCNT=(MAX*(MAX+1)//2)+1
dp=[[[[False]*(MAX) for _ in range(MAX)] for _ in range(MAX)] for _ in range(MAXCNT)]
#dic=defaultdict(str)
ans=[]

def DFS(cnt,a,b,c,res):
    if cnt>k:
        return
    
    if len(ans)>0:
        return 
    #print(idx,a,b,c,res,cnt)
    if a+b+c==n:
        if cnt==k:
            ans.append(res)
        return
    

    if dp[cnt][a][b][c]:
        return
    dp[cnt][a][b][c]=True

    DFS(cnt,a+1,b,c,res+'A')
    DFS(cnt+a,a,b+1,c,res+'B')
    DFS(cnt+a+b,a,b,c+1,res+'C') 

           


DFS(0,0,0,0,'')
print(ans[0] if len(ans)>0 else -1)