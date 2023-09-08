import sys
input=sys.stdin.readline
s1=input().rstrip('\n')
s2=input().rstrip('\n')
m=len(s1)
n=len(s2)

dp=[[""]*(m+1) for _ in range(n+1)]


for i in range(1,n+1):

    for j in range(1,m+1):
        if s1[j-1]==s2[i-1]:
            dp[i][j]=dp[i-1][j-1]+s1[j-1]
        else:
            l1=len(dp[i-1][j])
            l2=len(dp[i][j-1])
            if l1>l2:
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=dp[i][j-1]
                
if not dp[n][m]:
    print(0)
else:
    print(len(dp[n][m]))
    print(dp[n][m])