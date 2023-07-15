import sys
input=sys.stdin.readline
from itertools import combinations
n=int(input())
arr=[]
for i in range(n):
    sh,ss=map(int,input().split())
    arr.append([sh,ss])
ans=sys.maxsize
for i in range(1,n+1):
    arr1=list(combinations(arr,i))
    for cases in arr1:
        sh=1
        ss=0
        for j in range(len(cases)):
            sh*=cases[j][0]
            ss+=cases[j][1]
        ans=min(ans,abs(sh-ss))

print(ans)