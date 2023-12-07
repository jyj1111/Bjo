import sys
input=sys.stdin.readline

n,k=map(int,input().split())
num=input().rstrip('\n')
stack=[]

cnt=0
for i in range(n):
    
    while stack and int(stack[len(stack)-1])<int(num[i]) and cnt<k:
        stack.pop()
        cnt+=1
    stack.append(num[i])

if cnt<k:
    print(''.join(stack[:n-k]))

else:
    print(''.join(stack))