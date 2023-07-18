import sys
input=sys.stdin.readline
n,h=map(int,input().split())
H=[]
top=[0]*(h+1)
bot=[0]*(h+1)
for i in range(n):
  h1=int(input())
  if i%2==0:
    bot[h1]+=1
  else:
    top[h-h1+1]+=1

botPrefixSum=[0]*(h+2)
topPrefixSum=[0]*(h+2)
totalPrefixSum=[0]*(h+1)
for i in range(h):
  botPrefixSum[h-i]=botPrefixSum[h-i+1]+bot[h-i]
  topPrefixSum[i+1]=topPrefixSum[i]+top[i+1]
for i in range(1,h+1):
  totalPrefixSum[i]=botPrefixSum[i]+topPrefixSum[i]
totalPrefixSum.pop(0)

ans=min(totalPrefixSum)
cnt=totalPrefixSum.count(ans)
print(ans,cnt)