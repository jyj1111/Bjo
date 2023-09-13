import sys
input=sys.stdin.readline
from itertools import permutations

INF=sys.maxsize
N=int(input())
SCV=list(map(int,input().split()))
Mutal=[9,3,1]
if N<3:
    SCV+=[0]*(3-N)
X,Y,Z=SCV[0],SCV[1],SCV[2]

#print(X,Y,Z)        
dp=[[[INF]*(X+1)for _ in range(Y+1)] for _ in range(Z+1)]
dp[Z][Y][X]=0

for z in range(Z,-1,-1):
    for y in range(Y,-1,-1):
        for x in range(X,-1,-1):
            for dz,dy,dx in permutations(Mutal,3):
               z1=max(0,z-dz)
               y1=max(0,y-dy)
               x1=max(0,x-dx)
               #print(z1,y1,x1)
               dp[z1][y1][x1]=min(dp[z][y][x]+1,dp[z1][y1][x1])
               


print(dp[0][0][0])