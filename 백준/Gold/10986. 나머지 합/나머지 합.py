import sys
from collections import defaultdict
dic=defaultdict(int)
input=sys.stdin.readline
n,m=map(int,input().split())
arr=list(map(int,input().split()))
partsum=[0]*(n+1)
for i in range(1,n+1):
  partsum[i]=(partsum[i-1]+arr[i-1])%m

partsum.pop(0)

for i in range(n):
  dic[partsum[i]]+=1

answer=dic[0]

for key in dic:
  answer+=dic[key]*(dic[key]-1)//2
print(answer)