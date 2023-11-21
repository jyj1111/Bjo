import sys
input=sys.stdin.readline
n=int(input())
lines=[]
for i in range(n):
    l,r=map(int,input().split())
    lines.append((l,r))

lines.sort(key=lambda x:x[0])

start=lines[0][0]
end=lines[0][1]
ans=0

for i in range(1,n):
    l,r=lines[i]
    if l<=end and r>end:
        end=r
    elif l>end:
        ans+=end-start
        start=l
        end=r

ans+=end-start
print(ans)