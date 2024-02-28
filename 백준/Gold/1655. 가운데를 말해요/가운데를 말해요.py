import sys
from heapq import heappush,heappop
input=sys.stdin.readline

lmax=[]
rmin=[]

n=int(input())
for i in range(n):
    num=int(input())
    if len(lmax)<=len(rmin):
        if rmin and rmin[0]<num:
            heappush(lmax,-heappop(rmin))
            heappush(rmin,num)
        else:
            heappush(lmax,-num)
        
    else:
        if lmax and -lmax[0]>num:
            heappush(rmin,-heappop(lmax))
            heappush(lmax,-num)
        else:
            heappush(rmin,num)

    print(-lmax[0])