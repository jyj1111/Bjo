import sys
input=sys.stdin.readline
n=int(input())

arr=[]
for i in range(n+1):
    x,y=map(int,input().split())
    arr.append((x,y))
    
dy=[0,1,0,-1,0]
dx=[0,0,1,0,-1]


dp=[[sys.maxsize]*(n+1) for _ in range(5)]
length=0
y=arr[0][1]
x=arr[0][0]
tmp=[(x,y)]
for depth in range(1,n+1):
    for k in range(5):
        y1=arr[depth][1]+dy[k]
        x1=arr[depth][0]+dx[k]
        if 0<=y1<=100000 and 0<=x1<=100000:
            for x,y in tmp:
                dp[k][depth]=min(dp[k][depth],length+abs(y1-y)+abs(x1-x))
            
    tmp=[]       
    length=min(dp[0][depth],dp[1][depth],dp[2][depth],dp[3][depth],dp[4][depth])
    for k in range(5):
        if dp[k][depth]==length:
            y=arr[depth][1]+dy[k]
            x=arr[depth][0]+dx[k]
            tmp.append((x,y))

print(length)
