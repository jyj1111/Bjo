import sys
input=sys.stdin.readline
n=int(input())
s=list(input().rstrip('\n'))
if len(s)<=n:
    print(len(s))
else:
    l=0
    r=0
    ans=1
    s1=set()
    
    while l<=r and r<len(s):
        ##print(l,r)
        s1.add(s[r])
        ##print(s1)
        
        if len(s1)<=n:
            ans=max(ans,r-l+1)
            r+=1
            
        else:
            l+=1
            s1=set()
            r=l
            

    print(ans)