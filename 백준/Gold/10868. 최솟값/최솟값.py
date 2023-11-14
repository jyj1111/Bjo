import sys,math
input=sys.stdin.readline

N,M=map(int,input().split())#1<N,M<100000
MaxMax=1000000000
minNums=[MaxMax]*(2**(math.ceil(math.log2(N))+1))
mid=len(minNums)//2

for i in range(mid,mid+N):
    num=int(input())
    minNums[i]=num

for i in range(len(minNums)-1,1,-1):
    minNums[i//2]= min(minNums[i//2],minNums[i])

def segMin(lt,rt):
    segLt=lt+mid-1
    segRt=rt+mid-1
    segMin=MaxMax
    while segLt<segRt:
        if segLt%2==1:
            segMin=min(segMin,minNums[segLt])
        if segRt%2==0:
            segMin=min(segMin,minNums[segRt])
        segLt=(segLt+1)//2
        segRt=(segRt-1)//2

    if segLt==segRt:
        segMin=min(segMin,minNums[segLt])
    
    return segMin
    

for i in range(M):
    lt,rt=map(int,input().split())

    print(segMin(lt,rt))