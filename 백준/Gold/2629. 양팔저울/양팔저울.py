import sys
sys.setrecursionlimit(10 ** 9)
input=sys.stdin.readline

N=int(input())#1≤N≤30
weights=list(map(int,input().split()))
M=int(input())#1≤M<=7
checks=list(map(int,input().split()))
dp=[[0]*(15001) for i in range(31)]

def DFS(idx,hap):
    global dp
    #print(idx,hap)
    if idx>N:
        return
    if dp[idx][hap]:
        return
    
    dp[idx][hap]=1
    DFS(idx+1,hap+weights[idx-1])
    DFS(idx+1,hap)
    DFS(idx+1,abs(hap-weights[idx-1]))
           
    

DFS(0,0)
ans=[]
for check in checks:
    if check>15000:
        ans.append('N')
    elif dp[N][check]:
        ans.append('Y')
    else:
        ans.append('N')

print(*ans)