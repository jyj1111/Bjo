import sys
input=sys.stdin.readline

def init():
    dp=[[0]*15 for _ in range(15)]
    for i in range(1,15):
        dp[0][i]=i
    return dp
    

def Apt(k,n):
    dp=init()
    for i in range(1,k+1):
        for j in range(1,n+1):
            for t in range(1,j+1):
                dp[i][j]+=dp[i-1][t]
           
    return dp[k][n]

num=int(input())

for i in range(num):
    k=0
    n=0
    for j in range(2):
        if j==0:
            k=int(input())
        else:
            n=int(input())
    
    print(Apt(k,n))