import sys
input=sys.stdin.readline

n,m=map(int,input().split())
graph=[list(input().rstrip('\n')) for _ in range(n)]
parents=[0]*(n*m)
dic={'D':[1,0],'L':[0,-1],'R':[0,1], 'U':[-1,0]}

def init():
    for i in range(n*m):
        parents[i]=i        
            
            

def find(i):
    if parents[i]==i:
        return i
    parents[i]=find(parents[i])
    return parents[i] 
   

def union(i,j):
    i=find(i)
    j=find(j)
 
    if i==j:
        return
    elif i>j:
        parents[i]=j

    else:
        parents[j]=i    
  
init()
for i in range(n):
    for j in range(m):
        di,dj=dic[graph[i][j]]
        i1=i+di
        j1=j+dj
        union(i*m+j,i1*m+j1)
ans=set()
for i in range(n):
    for j in range(m):
        ans.add(find(i*m+j))

print(len(ans))        

