import sys
input=sys.stdin.readline
n=int(input())

ans=1000001

arr=[]
for i in range(n):
    t,s=map(int,input().split())
    arr.append((t,s))

arr.sort(key=lambda x:x[1])

time=0
for i in range(n):
    time+=arr[i][0]
    ans=min(ans,arr[i][1]-time)

if ans<0:
    print(-1)
else:
    print(ans)
    