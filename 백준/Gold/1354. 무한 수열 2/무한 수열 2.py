import sys,math
sys.setrecursionlimit(10**8)
input=sys.stdin.readline
from collections import defaultdict

dic=defaultdict(int)
n,p,q,x,y=map(int,input().split())

def DFS(num):
    if num<=0:
        dic[num]=1
        return 1
    else:
        if dic[num]>0:
           return dic[num]
        else:
           dic[num]=DFS(math.floor(num/p)-x)+DFS(math.floor(num/q)-y)
           #print(num,dic[num])
           return dic[num]
        
    
    
    

print(DFS(n))
