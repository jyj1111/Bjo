import sys
input=sys.stdin.readline
n,x=map(int,input().split())
arr=list(map(int,input().split()))
arr.sort()
l=0
r=n-1
ans=0
remain=0
while l<=r:
    if arr[r]==x:
        ans+=1
        r-=1
        continue
    if r==l:
        remain+=1
        break
    if arr[l]+arr[r]>=x/2:
        ans+=1
        l+=1
        r-=1
    else:
        remain+=1
        l+=1

    

print(ans+(remain)//3)