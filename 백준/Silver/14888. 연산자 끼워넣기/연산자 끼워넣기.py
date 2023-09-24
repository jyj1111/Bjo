import sys
input=sys.stdin.readline
import math

n=int(input())## 2<=n<=11
nums=list(map(int,input().split()))
operatorNums=list(map(int,input().split()))## +,-,*,//
operators=[]
for i in range(4):
    if i==0:
        operators+=['+']*(operatorNums[i])
    elif i==1:
        operators+=['-']*(operatorNums[i])
    elif i==2:
        operators+=['*']*(operatorNums[i])

    elif i==3:
        operators+=['/']*(operatorNums[i])


answers=[]
visitedOperators=[0]*(n-1)

def DFS(depth,result):
    global answers
    #print(depth,result,visitedOperators)
    if depth==n:
        #print(answers)
        answers.append(result)
    else:
        for i in range(n-1):
            if visitedOperators[i]==0:
                visitedOperators[i]=1
                if operators[i]=='+':
                    DFS(depth+1,result+nums[depth])

                elif operators[i]=='-':
                    DFS(depth+1,result-nums[depth])

                elif operators[i]=='*':
                    DFS(depth+1,result*nums[depth])

                elif operators[i]=='/':
                    DFS(depth+1,math.trunc(result/nums[depth]))
                visitedOperators[i]=0
                    
 
                
DFS(1,nums[0])
print(max(answers))
print(min(answers))