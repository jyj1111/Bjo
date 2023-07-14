import sys
input=sys.stdin.readline
n=int(input())
for i in range(n):
  num=int(input())
  secret=True
  for j in range(2,1000001):
    if num%j==0:
      print("NO")
      secret=False
      break
  if secret:
    print("YES")