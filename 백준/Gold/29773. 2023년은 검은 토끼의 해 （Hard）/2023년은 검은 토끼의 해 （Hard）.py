import sys,math
input=sys.stdin.readline


N=int(input())
A = [0]*20
for i in range(19, 0, -1):
    A[i] = N % 10
    N //= 10

x = [2, 0, 2, 3, -1]  
dp = [[[0]*2 for _ in range(5)] for _ in range(21)]
dp[0][0][0] = 1

for i in range(20):
    for j in range(5):
        for k in range(2):
            for l in range(10):
                if k or l < A[i]:
                    dp[i+1][j+(l==x[j])][1] += dp[i][j][k]

        dp[i+1][j+(A[i]==x[j])][0] += dp[i][j][0]

print(dp[20][4][0] + dp[20][4][1]) 