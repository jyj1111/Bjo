import sys
input=sys.stdin.readline
n=int(input())
dp=[100000]*(n*3+1)
dp[n]=0
i=n
while i>1:
  if i%2==0:
    dp[i//2]=min(dp[i]+1,dp[i//2])
  if i%3==0:
    dp[i//3]=min(dp[i]+1,dp[i//3])
  dp[i-1]=min(dp[i]+1,dp[i-1])  
  i=i-1

j=1
ans=[]
while True:
  ans.append(str(j))
  if dp[j]==0:
    break
  
  if dp[j*3]==dp[j]-1:
    j=j*3
  elif dp[j*2]==dp[j]-1:
    j=j*2
  elif dp[j+1]==dp[j]-1:
    j=j+1
print(dp[1])
print(" ".join(ans[::-1]))