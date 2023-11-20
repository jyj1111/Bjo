import sys
from collections import defaultdict
input=sys.stdin.readline

n=int(input())# n<=100000
arr=list(map(int,input().split()))
dic=defaultdict(int)

for i in range(n):
    dic[arr[i]]=0

l=0
r=0
dic[arr[0]]+=1
ans=n*(n+1)//2
while l<=r:
    
    if dic[arr[r]]>=2:
        ans-=(n-r)
        dic[arr[l]]-=1
        l+=1
        
    else:
        r+=1
        if r==n:
            break
        dic[arr[r]]+=1

print(ans)

    