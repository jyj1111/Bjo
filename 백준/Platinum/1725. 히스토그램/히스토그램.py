import sys
input=sys.stdin.readline
n=int(input())
highs=[]
for i in range(n):
    highs.append(int(input()))
highs+=[-1]
stack=[]
ans=0
for i in range(n+1):
    while stack and highs[stack[-1]]>highs[i]:
        j=stack.pop()
        l=0
        if len(stack)==0:
            l=i
        else:
            l=i-stack[-1]-1
            
        ans=max(ans,l*highs[j])
        
    stack.append(i)

print(ans)