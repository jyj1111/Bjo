import sys
input=sys.stdin.readline
inf=sys.maxsize
n=int(input())## n은 50이하
arrx=set()
arry=set()
arr=[]
cnt=0
for i in range(n):
    x,y=map(int,input().split())
    arr.append([x,y])
    arrx.add(x)
    arry.add(y)
arrx=list(arrx)
arry=list(arry)

ans=[inf]*(n)

for x1 in arrx:
    for y1 in arry:
        dis=[]
        for x,y in arr:
            dis.append(abs(x-x1)+abs(y-y1))
            
        dis.sort()
        
        sumdis=[0]*n
        sumdis[0]=dis[0]
        for i in range(1,n):
            sumdis[i]+=dis[i]+sumdis[i-1]
            
        for i in range(n):
            ans[i]=min(ans[i],sumdis[i])

print(*ans)