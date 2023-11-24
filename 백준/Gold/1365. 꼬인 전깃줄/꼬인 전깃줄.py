import sys
from bisect import bisect_left
input=sys.stdin.readline

N=int(input())
arr=list(map(int,input().split()))

stack=[]

for i in range(N):
    if stack and stack[-1]>=arr[i]:
        idx=bisect_left(stack,arr[i])
        stack[idx]=arr[i]

    else:
        stack.append(arr[i])

print(N-len(stack))