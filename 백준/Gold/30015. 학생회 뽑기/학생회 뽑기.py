import sys

input=sys.stdin.readline
n,k=map(int,input().split()) # 1<=n<=200000, 1<=k<=n
arr=list(map(int,input().split()))

ans=0

for i in range(19,-1,-1):
    cnt=0
    tmp=[]
    for num in arr:
        if num&(1<<i):
            tmp.append(num)

    if len(tmp)>=k:
         ans=ans|(1<<i)
         arr=tmp

                    
            

print(ans)