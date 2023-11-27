import sys
from collections import defaultdict
input=sys.stdin.readline

n,m=map(int,input().split())
Dict=defaultdict(int)

listeners=[]
for i in range(n):
    person=input().rstrip('\n')
    listeners.append(person)

listeners.sort()

for person in listeners:
    Dict[person]=0    
    
cnt=0

for j in range(m):
    person=input().rstrip('\n')
    if person in Dict:
        Dict[person]+=1
        cnt+=1

print(cnt)
for person in Dict:
    if Dict[person]>0:
        print(person)

