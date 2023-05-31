import sys
input=sys.stdin.readline
n,s=map(int,input().split())
nums=list(map(int,input().split()))
# 0,5,6,9,14,24,31,35,44,46,54
prefixSum=[0]*(n+1)
for i in range(n):
    prefixSum[i+1]=prefixSum[i]+nums[i]

l=0
r=0
ans=n+1
while l<=r and r<n:
    hap=prefixSum[r+1]-prefixSum[l]
    if hap>=s:
        ans=min(ans,r+1-l)  
        l+=1
    else:
        r+=1
if ans==n+1:
    print(0)
else:
    print(ans)
