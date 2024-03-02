import sys
input=sys.stdin.readline

n,m=map(int,input().split())
arr=[]
for _ in range(n):
    arr.append(int(input()))

lt=0
rt=max(arr)*m
ans=0

while lt<=rt:
    mid=(lt+rt)//2
    hap=sum([mid//item for item in arr])
        
    if hap>=m:
        ans=mid
        rt=mid-1
    else:
        lt=mid+1

print(ans)    
