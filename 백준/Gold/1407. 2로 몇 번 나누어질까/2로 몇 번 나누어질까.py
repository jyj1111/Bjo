import sys
input=sys.stdin.readline
import math
a,b=map(int,input().split())

def cnt(n):
  ans=n
  for i in range(1,61):
    ans+=(n//(2**i))*(2**(i-1))
  return ans

print(cnt(b)-cnt(a-1))