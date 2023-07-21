import sys
input=sys.stdin.readline

k=int(input())
def soinsu(num):
  arr=[]
  
  for i in range(2,int(num**0.5)+1):
    while num%i==0:
      arr.append(i)
      num=num//i
  if num!=1:
    arr.append(num)

  return [len(arr),arr] 

cnt,arr=soinsu(k)

print(cnt)
print(*arr)
