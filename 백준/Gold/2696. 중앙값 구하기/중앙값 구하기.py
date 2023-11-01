import sys,heapq
input=sys.stdin.readline

"""

"""

T=int(input())#T<1000
for i in range(T):
    M=int(input())#M<10000
    num=M//10
    Arr=[]
    for j in range(num+1):
        arr=list(map(int,input().split()))
        Arr+=arr
    print((M//2)+1)
    ans=[]
    for k in range(1,M+1,2):
        ans.append(sorted(Arr[:k])[k//2])

    num1=((M//2)+1)//10
    num2=((M//2)+1)%10
    for j in range(num1):
        print(*ans[j*10:(j+1)*10])

    print(*ans[-num2:])
        
       





    
"""
leftPQ=[]
rightPQ=[]
heapq.heapify(leftPQ)
heapq.heapify(rightPQ)


for cnt in range(1,N+1):
    num=int(input())
    if cnt%2==1:
        heapq.heappush(leftPQ,-num)

    else:
        heapq.heappush(rightPQ,num)

    if leftPQ and rightPQ and -leftPQ[0]>rightPQ[0]:
        mid1=-heapq.heappop(leftPQ)
        mid2=heapq.heappop(rightPQ)
        heapq.heappush(leftPQ,-mid2)
        heapq.heappush(rightPQ,mid1)
        
    print(-leftPQ[0])
    
"""