import sys
input=sys.stdin.readline
n,m=map(int,input().split())

back=[]
for i in range(n):
    l,r=map(int,input().split())
    if l>r:
        back.append((l,r))

back.sort(key=lambda x:x[1]) 
#print(back)
backStart=back[0][0]
backEnd=back[0][1]
ans=m

for i in range(1,len(back)):
    start,end=back[i]
    if start>backStart and end<=backStart:
        backStart=start
    elif end>backStart:
        #print(backStart,backEnd)
        ans+=2*(backStart-backEnd)
        backStart=start
        backEnd=end

ans+=2*(backStart-backEnd)
print(ans)