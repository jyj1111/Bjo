import sys,math
input=sys.stdin.readline

N,M=map(int,input().split())#1<N,M<100000
MaxMax=1000000000
maxNums=[0]*(2**(math.ceil(math.log2(N))+1))
minNums=[MaxMax]*(2**(math.ceil(math.log2(N))+1))
mid=len(maxNums)//2

for i in range(mid,mid+N):
    num=int(input())
    maxNums[i]=num
    minNums[i]=num

for i in range(len(maxNums)-1,1,-1):
    maxNums[i//2]= max(maxNums[i//2],maxNums[i])
    minNums[i//2]= min(minNums[i//2],minNums[i])

def segMaxMin(lt,rt):
    segLt=lt+mid-1
    segRt=rt+mid-1
    segMax=0
    segMin=MaxMax
    while segLt<segRt:
        if segLt%2==1:
            segMax=max(segMax,maxNums[segLt])
            segMin=min(segMin,minNums[segLt])
        if segRt%2==0:
            segMax=max(segMax,maxNums[segRt])
            segMin=min(segMin,minNums[segRt])

        segLt=(segLt+1)//2
        segRt=(segRt-1)//2

    if segLt==segRt:
        segMax=max(segMax,maxNums[segLt])
        segMin=min(segMin,minNums[segLt])
    
    return [segMin,segMax]
    

for i in range(M):
    lt,rt=map(int,input().split())

    print(*segMaxMin(lt,rt))