import sys
input=sys.stdin.readline
case=int(input())
for i in range(case):
  days=int(input())
  stocks=list(map(int,input().split()))
  profit=0
  mx=0
  for j in range(days-1,-1,-1):
    if mx<stocks[j]:
      mx=stocks[j]
      
    else:
      profit+=mx-stocks[j]
  print(profit)
      