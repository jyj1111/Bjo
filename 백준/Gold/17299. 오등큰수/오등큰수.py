import sys
from collections import defaultdict
count=defaultdict(int)
input=sys.stdin.readline
n=int(input())
A=list(map(int,input().split()))
for num in A:
    count[num]+=1
# 1 1 2 3 4 2 1
# 3 3 2 1 1 2 3
# 0 1 2 3 4
stack=[]
ans=[-1]*(n)
for i in range(n):
    while stack and count[A[stack[-1]]]<count[A[i]]:
        ans[stack.pop()]=A[i]

    stack.append(i)

print(' '.join(list(map(str,ans))))
