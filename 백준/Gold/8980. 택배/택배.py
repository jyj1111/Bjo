import sys
input=sys.stdin.readline
        
N,C=map(int,input().split())
M=int(input())
arr=[]
for i in range(M):
    start,end,value=map(int,input().split())
    arr.append((start,end,value))

arr.sort(key=lambda x:(-x[1],-x[0]))
capacity=[0]*(N+1)

ans=0
for start,end,value in arr:
    #print(start,end,value)
    #print(capacity)
    tmp=0
    if capacity[end]+value<=C:
        tmp=value
    else:
        tmp=C-capacity[end]
       
    for j in range(end,start,-1):
        capacity[j]+=tmp
    ans+=tmp
   

print(ans)