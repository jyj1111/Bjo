import sys
input=sys.stdin.readline
n=int(input())
k=int(input())

start=1
end=n**2
ans=end
while start<=end:
    mid=(start+end)//2
    hap=0
    for row in range(1,n+1):
        hap+=min(n,mid//row)

    if hap>=k:
        ans=min(ans,mid)
        end=mid-1
        
    else:
        start=mid+1

print(ans)
        