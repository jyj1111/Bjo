import sys
input=sys.stdin.readline
d,n,m=map(int,input().split())## d는 10억 이하 n은 50000이하 m은 n이하
arr=[]
for i in range(n):
    jump=int(input())
    arr.append(jump)
arr.append(d)
arr.sort()

lt=0
rt=d
ans=0
while lt<=rt:
    mid=(lt+rt)//2
    start=0
    cnt=0
    for i in range(n+1):
        if arr[i]-start<mid:
            cnt+=1

        else:
            start=arr[i]

    if cnt>m:
        rt=mid-1
    else:
        lt=mid+1
        ans=mid
            
print(ans)            