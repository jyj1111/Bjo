import sys
input=sys.stdin.readline
from collections import defaultdict

target=int(input())
n,m=map(int,input().split())
A=2*[int(input()) for _ in range(n)]
B=2*[int(input()) for _ in range(m)]

def makePrefixSum(arr,num):
    prefixSum=[0]*(num+1)
    for i in range(num):
        prefixSum[i+1]=prefixSum[i]+arr[i]
    return prefixSum
    

def makeDic(num,arr):
    dic=defaultdict(int)
    prefixSum=makePrefixSum(arr,2*num)
    for r in range(1,num):
        for i in range(num):
            partSum=prefixSum[i+r]-prefixSum[i]
            if partSum<=target: dic[partSum]+=1

    if prefixSum[num]<=target: dic[prefixSum[num]]=1
    return dic

dicA=makeDic(n,A)
dicB=makeDic(m,B)

ans=dicA[target]+dicB[target]

for num in dicA:
    if dicB[target-num]>0:
        ans+=dicA[num]*dicB[target-num]

print(ans)
