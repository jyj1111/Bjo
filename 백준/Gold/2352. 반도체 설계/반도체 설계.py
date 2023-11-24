import sys
from bisect import bisect_left
input=sys.stdin.readline
# 10 20 5 30 18 50
N=int(input())# 1<=N<=1000000
arr=list(map(int,input().split()))

stack=[]

for i in range(N):
    if stack and stack[-1]>=arr[i]:
        idx=bisect_left(stack,arr[i])
        stack[idx]=arr[i]

    else:
        stack.append(arr[i])

print(len(stack))
        