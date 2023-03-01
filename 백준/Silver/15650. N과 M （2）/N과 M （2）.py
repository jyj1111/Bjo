import sys
input=sys.stdin.readline
n,m=map(int,input().split())
checked=[0]*(n+1)
answer=[0]*(m+1)
def DFS(idx):
    
    if idx==m+1:
        for i in range(1,m+1):
            print(answer[i],end=' ')
        print()
        
    elif idx>m+1:
        return
    else:
        for i in range(1,n+1):
            if max(answer)<i:
                answer[idx]=i
                DFS(idx+1)
                answer[idx]=0

DFS(1)