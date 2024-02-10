import sys
input=sys.stdin.readline
from collections import defaultdict

people=[]
n=int(input())

for i in range(n):
    flag,pos=map(int,input().split())
    people.append((pos,flag))

people.sort()
        
wmDiff=[0]*(n+1)

for i in range(n):
    pos,flag=people[i]
    if flag:
        wmDiff[i+1]=wmDiff[i]+1
    else:
        wmDiff[i+1]=wmDiff[i]-1

dic=defaultdict(list)

for i in range(n+1):
    dic[wmDiff[i]].append(i)

ans=0

for key,value in dic.items():
    n=len(value)
    if n>1:
        ans=max(ans,people[value[-1]-1][0]-people[value[0]][0])
        

print(ans)
    