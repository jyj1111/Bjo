import sys
input=sys.stdin.readline
n=int(input())
arr=[]
population=0
for i in range(n):
    location,num=map(int,input().split())
    arr.append((location,num))
    population+=num
arr.sort(key=lambda x:x[0])
cnt=0
for location,num in arr:
    cnt+=num
    if cnt>=population/2:
        print(location)
        break