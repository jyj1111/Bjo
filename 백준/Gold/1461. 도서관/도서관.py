import sys
input=sys.stdin.readline
        
n,m=map(int,input().split())
arr=list(map(int,input().split()))
arr.sort()

minusArr=[]
plusArr=[]

for i in range(n):
    if arr[i]<0:
        minusArr.append(arr[i])
    else:
        plusArr.append(arr[i])

plusArr.sort(key=lambda x:-x)

ans=0

if plusArr and minusArr:
    if plusArr[0]>abs(minusArr[0]):
        ans=plusArr[0]
        for i in range(m,len(plusArr),m):
            ans+=2*plusArr[i]
        for i in range(0,len(minusArr),m):
            ans+=2*abs(minusArr[i])

    else:
        ans=abs(minusArr[0])
        for i in range(m,len(minusArr),m):
            ans+=2*abs(minusArr[i])
        for i in range(0,len(plusArr),m):
            ans+=2*plusArr[i]
            
elif plusArr:
    ans=plusArr[0]
    for i in range(m,len(plusArr),m):
        ans+=2*plusArr[i]

elif minusArr:
    ans=abs(minusArr[0])
    for i in range(m,len(minusArr),m):
        ans+=2*abs(minusArr[i])

print(ans)