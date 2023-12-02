import sys
input=sys.stdin.readline
n,k=map(int,input().split())
arr=[0]*(1000001)
cnt=[0]*(1000001)

for i in range(n):
    start,end=map(int,input().split())
    arr[start]+=1
    arr[end]-=1


for i in range(1,1000001):
    cnt[i]=cnt[i-1]+arr[i-1]
    


hap=0
l=0
r=0

answer=[]


while l<=r:
    #print(l,r,hap)
    if hap<k:
        r+=1
        if r==1000001:
            break
        hap+=cnt[r]
        
    elif hap==k:
        answer.append([l,r])
        break
       
    else:
        l+=1
        hap-=cnt[l]

        
if not answer:
    print("0 0")
else:
    print(*answer[0])