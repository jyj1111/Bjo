import sys
import math
input=sys.stdin.readline
n=int(input())
arr=list(map(int,input().split()))
cnt=0
def prime(n):
    if n<=1:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
     
    return True
for num in arr:
    if prime(num):
        cnt+=1
print(cnt)