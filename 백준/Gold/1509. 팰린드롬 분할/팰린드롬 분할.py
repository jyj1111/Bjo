import sys
sys.setrecursionlimit(10**8)
input=sys.stdin.readline

S=input().rstrip('\n') # 1 ≤ S ≤ 2500
PalinDp=[[-1]*(len(S)) for _ in range(len(S))]
Dp=[2500]*(len(S)+1)
Dp[-1]=0
def isPalin(i,j):
    if PalinDp[i][j]!=-1:
        return PalinDp[i][j]
    if i==j:
        return 1
    if i+1==j:
        if S[i]==S[j]:
            return 1
        else:
            return 0

    PalinDp[i][j]=0
    if S[i]==S[j] and isPalin(i+1,j-1):
        PalinDp[i][j]=1
    return PalinDp[i][j]

for end in range(len(S)):
    for start in range(end + 1):
        if isPalin(start,end):
            Dp[end] = min(Dp[end], Dp[start - 1] + 1)
        else:
            Dp[end] = min(Dp[end], Dp[end - 1] + 1)
        

print(Dp[(len(S)-1)])