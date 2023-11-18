import sys
input=sys.stdin.readline
n=int(input())
tops=[]
for i in range(n):
    tops.append(int(input()))
tops+=[1000000001]
stack=[]
answer=0
for i in range(n+1):
    while stack and tops[stack[-1]]<=tops[i]:
        j=stack.pop()
        answer+=i-j-1
        
    stack.append(i)

print(answer)