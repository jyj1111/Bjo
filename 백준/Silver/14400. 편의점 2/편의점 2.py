import sys
input=sys.stdin.readline
n=int(input())## n은 100000이하
arr=[list(map(int,input().split())) for _ in range(n)]
mid_x=sorted(arr,key=lambda x:x[0])[n//2][0]
mid_y=sorted(arr,key=lambda x:x[1])[n//2][1]
res=0
for x,y in arr:
    res+=abs((x-mid_x))+abs((y-mid_y))

print(res)