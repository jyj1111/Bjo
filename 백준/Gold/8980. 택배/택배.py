import sys
input=sys.stdin.readline
        
N,C=map(int,input().split())
M=int(input())
arr=[]
for i in range(M):
    start,end,value=map(int,input().split())
    arr.append((start,end,value))

arr.sort(key=lambda x:(x[1],x[0]))
capacity=[0]*(N+1)

ans=0
for start,end,value in arr:
    #print(start,end,value)
    #print(capacity)
    tmp=value
    for j in range(start,end):
        tmp=min(tmp,C-capacity[j])
    #print(tmp)       
    for j in range(start,end):
        capacity[j]+=tmp
    ans+=tmp
   

print(ans)