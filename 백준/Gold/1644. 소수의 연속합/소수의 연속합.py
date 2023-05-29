import sys
input=sys.stdin.readline
n=int(input())
arr=[True]*(n+1)
for i in range(2,int(n**0.5)+1):
  if arr[i]==True:
    j=2
    while i*j<=n:
      arr[i*j]=False
      j+=1
 
prime=[]
for i in range(2,n+1):
  if arr[i]:
    prime.append(i)

l=0
r=0
answer=0
hap=0
while l<=r and r<len(prime):
  hap=sum(prime[l:r+1])
  if hap==n:
    answer+=1
    r+=1
  elif hap<n:
    r+=1
  elif hap>n:
    l+=1
    
  
print(answer)
