import sys
input=sys.stdin.readline

N=int(input())#1 ≤ N ≤ 2,000
nums=list(map(int,input().split()))
M=int(input())#1 ≤ M ≤ 1,000,000
dp=[[-1]*(N) for _ in range(N)]
for i in range(N):
    dp[i][i]=1

def Palindrome(S,E):
    if dp[S-1][E-1]!=-1:
        return dp[S-1][E-1]
    
        
    mid=((S-1)+(E-1))//2
    for i in range(mid,S-2,-1):
        if nums[i]==nums[E-1+S-1-i]:
            dp[i][E-1+S-1-i]=1
        else:
            for j in range(i,S-2,-1):
                dp[j][E-1+S-1-j]=0
            break
            
    return dp[S-1][E-1]
    
        

for i in range(M):
    S,E=map(int,input().split())
    print(Palindrome(S,E))