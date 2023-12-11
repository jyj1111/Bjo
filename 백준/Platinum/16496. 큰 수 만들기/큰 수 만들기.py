import sys
from functools import cmp_to_key
input=sys.stdin.readline
n=int(input())
arr=list(map(str,input().split()))


def compare(x,y):
    if x+y>y+x:
        return -1
    elif x+y<y+x:
        return 1
    else:
        return 0

arr.sort(key=cmp_to_key(compare))

if arr[0]=='0':
    print('0')
else:
    print("".join(arr))