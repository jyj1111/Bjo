import sys
input=sys.stdin.readline
n=int(input())
arr=list(map(int,input().split()))

visited=[0]*(n)
numSet=set()
hap=sum(arr)

def DFS(idx,hap):
    
    if idx>=n:
        if hap>0:
            numSet.add(hap)                               
        return
    else:
        DFS(idx+1,hap+arr[idx])
        DFS(idx+1,hap)
        DFS(idx+1,hap-arr[idx])
      
 


DFS(0,0)
print(hap-len(numSet))