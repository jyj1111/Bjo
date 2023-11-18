import sys
input=sys.stdin.readline
n=int(input())
tops=[100000001]+list(map(int,input().split()))
stack=[]
answer=[0]*(n+1)
for i in range(n,0,-1):
    while stack and tops[stack[-1]]<tops[i]:
        answer[stack.pop()]=i

    stack.append(i)

print(*answer[1:])