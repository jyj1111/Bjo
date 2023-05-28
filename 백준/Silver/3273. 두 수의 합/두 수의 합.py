import sys
input=sys.stdin.readline
n=int(input())
arr=list(map(int,input().split()))
arr.sort()
target=int(input())
l=0
r=n-1
answer=0
while l<r:
  if arr[l]+arr[r]==target:
    answer+=1
    r-=1
  elif arr[l]+arr[r]<target:
    l+=1
  elif arr[l]+arr[r]>target:
    r-=1

print(answer)