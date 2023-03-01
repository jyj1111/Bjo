import sys
input=sys.stdin.readline
n,m=map(int,input().split())
arr=list(map(int,input().split()))
arr.sort()
checked=[0]*(n+1)
answer=[]

def DFS(idx):
    
    if idx==m+1:
        for num in answer:
            print(num,end=' ')
        print()
        
    elif idx>m+1:
        return
    else:
        for i in range(1,n+1):
            if not checked[i]:
                checked[i]=1
                answer.append(arr[i-1])
                DFS(idx+1)
                checked[i]=0
                answer.pop()

DFS(1)