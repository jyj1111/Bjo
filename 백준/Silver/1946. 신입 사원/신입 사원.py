import sys
input=sys.stdin.readline

t=int(input())

for i in range(t):
    n=int(input())
    arr=[]
    for j in range(n):
        document,interview=map(int,input().split())
        arr.append((document,interview))

    arr.sort(key=lambda x:x[0])

    start=arr[0][0]
    end=arr[0][1]
    cnt=1
    for j in range(1,n):
        if arr[j][1]<end:
            end=arr[j][1]
            cnt+=1
    print(cnt)