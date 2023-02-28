import sys
input=sys.stdin.readline
a,b=map(int,input().split())
answer=[]

def DFS(start,idx):
    
    if start==b:
        answer.append(idx)
    elif start>b:
        return
    else:
        DFS(start*2,idx+1)
        DFS((start*10)+1,idx+1)

DFS(a,1)
if len(answer)==0:
    print(-1)
else:
    print(min(answer))