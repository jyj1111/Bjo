import sys
input=sys.stdin.readline
sys.setrecursionlimit(10 ** 9)
n=int(input())
arr=list(map(int,input().split()))
dp=[[0]*((500*30)+1) for _ in range(31)]

def DFS(depth,result):
    global dp
    #print(depth,result)
    if depth>n:
        return
    if dp[depth][result]:
        return 
    dp[depth][result]=1
    DFS(depth+1,result+arr[depth-1])
    DFS(depth+1,result)
    DFS(depth+1,abs(result-arr[depth-1]))
    
    
DFS(0,0)
#print(dp)

m=int(input())
ans=[]
cases=list(map(int,input().split()))
for case in cases:
    if case>15000:
        ans.append('N')     
        
    elif dp[n][case]:
        ans.append('Y')
        
    else:
        ans.append('N')

print(*ans)
        