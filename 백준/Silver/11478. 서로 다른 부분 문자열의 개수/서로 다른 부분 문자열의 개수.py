import sys
from collections import defaultdict
input=sys.stdin.readline

s=input().rstrip('\n')
n=len(s)
Dict=defaultdict(int)

for l in range(1,n+1):
    for i in range(n):
        if i+l<=n:
            Dict[s[i:i+l]]+=1

print(len(Dict.keys()))
            