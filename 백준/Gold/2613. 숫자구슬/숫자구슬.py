import sys
input=sys.stdin.readline
N,M=map(int,input().split())## N은 300이하, M은 N이하
arr=list(map(int,input().split()))

lt=max(arr)
rt=sum(arr)
ans=0

while lt<=rt:
    ##print(lt,rt)
    mid=(lt+rt)//2
    cnt=1
    hap=0
    for i in range(N):
        hap+=arr[i]
        if hap>mid:
            cnt+=1
            hap=arr[i]
          
    if cnt<=M:
        ans=mid
        rt=mid-1
        
    else:
        lt=mid+1

cntArr=[]
hap=0
idx=0
for i in range(N):
    hap+=arr[i]
    if hap>ans:
        cntArr.append(str(i-idx))
        hap=arr[i]
        idx=i
    elif hap<=ans and N-i<M-len(cntArr):
        cntArr+=["1"]*(N-i)
        idx=N-1
        break
cntArr.append(str(N-idx)) 

print(ans)
print(' '.join(cntArr))