import sys
input=sys.stdin.readline

n=int(input())
arr=list(map(int,input().split()))
prefixSum=[0]*(n+1)

val=sum(arr)

if val%4==0:
    k=val//4
    for i in range(n):
        prefixSum[i+1]=prefixSum[i]+arr[i]

    v1,v2,v3=0,0,0
    for i in range(n):
        if prefixSum[i]==3*k:
            v3+=v2
        elif prefixSum[i]==2*k:
            v2+=v1

        elif prefixSum[i]==k:
            v1+=1

    print(v3)
            
    

else:
    print(0)
