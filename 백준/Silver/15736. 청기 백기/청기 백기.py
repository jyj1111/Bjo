import sys
input=sys.stdin.readline
import math
n=int(input())
'''def cnt(num):
  cnt=0
  for i in range(1,num+1):
    if num%i==0:
      cnt+=1
  return cnt
ans=0
for i in range(1,n+1):
  if cnt(i)%2==1:
    ans+=1'''

print(math.floor(n**0.5))

