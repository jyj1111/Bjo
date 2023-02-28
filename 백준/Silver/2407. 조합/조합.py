import sys
input=sys.stdin.readline
n,m=map(int,input().split())
def factorial(k):
    result=1
    if k==0:
        return 1
    for i in range(1,k+1):
        result*=i
    return result   

print(factorial(n)//(factorial(m)*factorial(n-m)))