import sys
sys.setrecursionlimit(10**9)
input=sys.stdin.readline

n=int(input())
arr=list(map(int,input().split()))
hap=sum(arr)

dp=[['N']*(hap+1) for _ in range(n+1)]

def DFS(depth,value):
    if dp[depth][value]=='Y':
        return
    dp[depth][value]='Y'
    if depth==n:
        return
    
    DFS(depth+1,value+arr[depth])
    DFS(depth+1,value)
    DFS(depth+1,abs(value-arr[depth]))

DFS(0,0)

m=int(input())
arr1=list(map(int,input().split()))
ans=[]
for num in arr1:
    if num>hap:
        ans.append('N')
    else:
        ans.append(dp[n][num])        
    

print(*ans)