import sys
input=sys.stdin.readline
from itertools import combinations
n=int(input())
mp,mf,ms,mv=map(int,input().split())
arr=[]
for i in range(n):
    p,f,s,v,c=map(int,input().split())
    arr.append([p,f,s,v,c,i+1])
ans=sys.maxsize
ans1=[-1]
for i in range(1,n+1):
    arr1=list(combinations(arr,i))
    for cases in arr1:
        p1=0
        f1=0
        s1=0
        v1=0
        c1=0
        for j in range(len(cases)):
            p1+=cases[j][0]
            f1+=cases[j][1]
            s1+=cases[j][2]
            v1+=cases[j][3]
            c1+=cases[j][4]
        if p1<mp or f1<mf or s1<ms or v1<mv:
            continue
        if c1<=ans:
            if c1<ans:
                ans=c1
                tmp=[]
                for p,f,s,v,c,num in cases:
                    tmp.append(num)
                ans1=[-1]
                ans1[0]=tmp
            else:
                tmp=[]
                for p,f,s,v,c,num in cases:
                    tmp.append(num)
                ans1.append(tmp)
ans1.sort()
if ans1[0]==-1:
    print(-1)
else:
    print(ans)
    print(*ans1[0])
