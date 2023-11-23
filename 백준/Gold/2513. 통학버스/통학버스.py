import sys
input=sys.stdin.readline
apartNum,busCapacity,schoolPos=map(int,input().split())

leftAparts=[]
rightAparts=[]

for i in range(apartNum):
    pos,num=map(int,input().split())
    if pos<schoolPos:
        leftAparts.append((pos,num))
    else:
        rightAparts.append((pos,num))
        
leftAparts.sort(key=lambda x:x[0])
rightAparts.sort(key=lambda x:-x[0])

ans=0

if leftAparts:
    lidx=0
    lpos=leftAparts[lidx][0]
    lstudents=leftAparts[lidx][1]  
    while lpos<schoolPos and lidx<len(leftAparts):
        if lstudents<=busCapacity:
            lidx+=1
            if lidx==len(leftAparts):
                break
        
            lstudents+=leftAparts[lidx][1]

        else:
            lstudents-=busCapacity
            ans+=2*(schoolPos-lpos)
            lpos=leftAparts[lidx][0]
    ans+=2*(schoolPos-lpos)
    #print(lpos,lstudents)
    #print(ans)

if rightAparts:
    ridx=0
    rpos=rightAparts[ridx][0]
    rstudents=rightAparts[ridx][1]
    while rpos>schoolPos and ridx<len(rightAparts):
        if rstudents<=busCapacity:
            ridx+=1
            if ridx==len(rightAparts):
                break
        
            rstudents+=rightAparts[ridx][1]

        else:
            rstudents-=busCapacity
            ans+=2*(rpos-schoolPos)
            rpos=rightAparts[ridx][0]
    ans+=2*(rpos-schoolPos)
    #print(rpos,rstudents)
    #print(ans)

print(ans)