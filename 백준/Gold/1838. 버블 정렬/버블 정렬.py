import sys
from collections import defaultdict
input=sys.stdin.readline
n=int(input())
nums=list(map(int,input().split()))
sortedNums=sorted(nums)

dic,dic1=defaultdict(int), defaultdict(int)

for i in range(n):
    dic[nums[i]]=i

for i in range(n):
    dic1[sortedNums[i]]=i

ans=0
for num in nums:
    ans=max(ans,dic[num]-dic1[num])

print(ans)