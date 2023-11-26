import sys,math
sys.setrecursionlimit(10**8)
input=sys.stdin.readline
from collections import defaultdict

dic=defaultdict(int)
dic[0]=1
n,p,q=map(int,input().split())

def DFS(num):
    if num==0:
        return 1
    else:
        if dic[num]>0:
           return dic[num]
        else:
           dic[num]=DFS(math.floor(num/p))+DFS(math.floor(num/q))
           #print(num,dic[num])
           return dic[num]
        
    
    
    

print(DFS(n))