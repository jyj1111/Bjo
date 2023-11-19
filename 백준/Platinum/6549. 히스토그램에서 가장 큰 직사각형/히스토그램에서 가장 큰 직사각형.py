import sys,copy
input=sys.stdin.readline
while True:
    test=list(map(int,input().split()))
    if test[0]==0:
        break
    n=test[0]
    highs=copy.deepcopy(test[1:])
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