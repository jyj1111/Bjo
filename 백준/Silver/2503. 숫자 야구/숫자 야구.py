import sys
input=sys.stdin.readline
n=int(input())
arr=[]
def split(n):
  n1=n//100
  n=n%100
  n2=n//10
  n=n%10
  return [n1,n2,n]
 

def judge(n,m):
  arr1=split(n)
  arr2=split(m)
  strike=0
  ball=len(set(arr1)&set(arr2))
  for k in range(3):
    if arr1[k]==arr2[k]:
      strike+=1
      ball-=1
  return [strike,ball]
     
  
for i in range(n):
  cases=[]
  num,strike,ball=map(int,input().split())
  for j in range(123,1000):
    if len(set(split(j)))<3 or 0 in set(split(j)):
      continue
    strike1,ball1=judge(j,num)
    if strike1==strike and ball1==ball:
      cases.append(j)
  if not arr:
    arr.append(cases)
  else:
    arr[0]=list(set(arr[0])&set(cases))

print(len(arr[0]))