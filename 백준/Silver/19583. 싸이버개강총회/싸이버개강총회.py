import sys
input=sys.stdin.readline
from collections import defaultdict
dic=defaultdict(int)
start,end,stop=input().split()
cnt=0

def timeToNum(s):
    hour,minute=map(int,s.split(':'))
    return 60*hour+minute

while True:
    try:
       time,member=input().split()
       if 0<=timeToNum(time)<=timeToNum(start):
           dic[member]=1
       if timeToNum(end)<=timeToNum(time)<=timeToNum(stop):
           if dic[member]>0:
               cnt+=1
               dic[member]-=1
    except:
        break

print(cnt)