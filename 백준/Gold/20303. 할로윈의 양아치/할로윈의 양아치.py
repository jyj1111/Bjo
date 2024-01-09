import sys
from collections import defaultdict
sys.setrecursionlimit(10**8)
input=sys.stdin.readline

dic=defaultdict(list)

n,m,k=map(int,input().split())
candies=[0]+list(map(int,input().split()))

parents=[0]*(n+1)

def init():
    for i in range(1,n+1):
        parents[i]=i

def find(a):
    if parents[a]==a:
        return a
    parents[a]=find(parents[a])
    return parents[a] 
   

def union(a,b):
    a=find(a)
    b=find(b)
    if a==b:
        return
    elif a>b:
        parents[a]=b

    else:
        parents[b]=a    

init()
for i in range(m):
    f1,f2=map(int,input().split())
    union(f1,f2)    

for i in range(1,n+1):
    dic[find(i)].append(i)
        
arr=[]
for key,values in dic.items():
    hap=0
    for value in values:
        hap+=candies[value]
    arr.append((len(values),hap))

#print(dic)
    
dp=[0]*(k)

arr.sort(key=lambda x:(x[0],x[1]))

for v,w in arr:
    for i in range(k-1,v-1,-1):
        dp[i]=max(dp[i],dp[i-v]+w)

print(max(dp))