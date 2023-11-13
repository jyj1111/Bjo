import sys,math
input=sys.stdin.readline

N,M,K=map(int,input().split())#1<N,M<1000

nums=[0]*(2**(math.ceil(math.log2(N))+1))
mid=len(nums)//2
for i in range(mid,mid+N):
    nums[i]=int(input())

for i in range(len(nums)-1,1,-1):
    nums[i//2]+=nums[i]


def segUpdate(idx,updateNum):
    segIdx=idx+mid-1
    changeNum=updateNum-nums[segIdx]
    
    while segIdx>0:
        nums[segIdx]+=changeNum
        segIdx=segIdx//2

def segHap(lt,rt):
    segLt=lt+mid-1
    segRt=rt+mid-1
    segHap=0
    while segLt<segRt:
        if segLt%2==1:
            segHap+=nums[segLt]
        if segRt%2==0:
            segHap+=nums[segRt]

        segLt=(segLt+1)//2
        segRt=(segRt-1)//2

    if segLt==segRt:
        segHap+=nums[segLt]
    
    return segHap
    

for i in range(M+K):
    flag,num1,num2=map(int,input().split())

    if flag==1:
        segUpdate(num1,num2)
    elif flag==2:
        print(segHap(num1,num2))