import sys,heapq
input=sys.stdin.readline
MAX=sys.maxsize
t=int(input())

dp1=[MAX]*(101)

dp1[2]=1
dp1[3]=7
dp1[4]=4
dp1[5]=2
dp1[6]=6
dp1[7]=8

for i in range(8,101):
    for j in range(2,8):
        if i>=j:
            if j!=6:
                dp1[i]=min(dp1[i],dp1[i-j]*10+dp1[j])
            else:
                dp1[i]=min(dp1[i],dp1[i-j]*10)


arr1=[0]*(101)

for i in range(2,101):
    if i%2==0:
        arr1[i]=int('1'*(i//2))
    else:
        arr1[i]=int('7'+'1'*((i-3)//2))
    
            
            


for i in range(t):
    num=int(input())
    print(dp1[num],arr1[num])