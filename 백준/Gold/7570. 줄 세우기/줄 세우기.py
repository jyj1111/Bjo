import sys
input=sys.stdin.readline

n=int(input())
location=[0]*(n+1)
lines=list(map(int,input().split()))
lines.insert(0,0)
for i in range(n+1):
    location[lines[i]]=i

cnt=1
mx=1
for i in range(1,n):
    if location[i+1]>location[i]:
        cnt+=1
        mx=max(cnt,mx)
    else:
        cnt=1

print(n-mx)