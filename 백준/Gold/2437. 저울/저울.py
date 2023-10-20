import sys
input=sys.stdin.readline
"""
1 1 2 3 6 7 30
"""

N=int(input())
weights=list(map(int,input().split()))
weights.sort()
hap=1
for weight in weights:
    if hap<weight:
        break
    else:
        hap+=weight

print(hap)