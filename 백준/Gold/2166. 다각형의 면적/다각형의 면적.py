import sys
input=sys.stdin.readline
"""
0 a c 0
0 b d 0
"""

N=int(input())#3 ≤ N ≤ 10,000
Points=[list(map(int,input().split())) for _ in range(N)]
Points.append(Points[0])
s1=0
s2=0
for i in range(N):
    s1+=Points[i][0]*Points[i+1][1]
    s2+=Points[i][1]*Points[i+1][0]

print(round(abs(s1-s2)/2,1))