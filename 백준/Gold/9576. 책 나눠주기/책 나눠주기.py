import sys
input=sys.stdin.readline

t=int(input())

for i in range(t):
    n,m=map(int,input().split())
    bookRange=[]
    visited=[0]*(n+1)
    for j in range(m):
        a,b=map(int,input().split())
        bookRange.append((a,b))
    bookRange.sort(key=lambda x:(x[1],x[0]))
    ans=0
    for start,end in bookRange:
        for num in range(start,end+1):
            if not visited[num]:
                visited[num]=1
                ans+=1
                break

    print(ans)