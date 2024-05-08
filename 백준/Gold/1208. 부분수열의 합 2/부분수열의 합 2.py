import sys
from itertools import combinations
from collections import defaultdict

input=sys.stdin.readline
n,s=map(int,input().split())
nums=list(map(int,input().split()))

mid=n//2
lnums,rnums=nums[:mid],nums[mid:]
ldic,rdic=defaultdict(int),defaultdict(int)

for i in range(1,mid+1):
    for arr in combinations(lnums,i):
        ldic[sum(arr)]+=1

for j in range(1,n-mid+1):
    for arr in combinations(rnums,j):
        rdic[sum(arr)]+=1

ans=ldic[s]+rdic[s]

for num in ldic:
    if s-num in rdic:
        ans+=ldic[num]*rdic[s-num]

print(ans)