import sys
input=sys.stdin.readline

n=int(input())
arr=list(map(int,input().split()))

stones=[[i] for i in arr]

cnt=n

for i in range(n-1):
    for stone in stones[i]:
        if stone<arr[i+1]:
            stones[i+1].append(arr[i+1]-stone)

        elif stone==arr[i+1]:
            stones[i+1]=[]
            cnt-=1
            break
            

print(cnt)       