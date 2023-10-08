import sys
input=sys.stdin.readline
N=int(input()) #4 ≤ N ≤ 20 , N은 짝수

abilities=[list(map(int,input().split())) for _ in range(N)]
visited=[0]*(N)
ans=sys.maxsize

def DFS(end):
    global ans
    if visited.count(1)==N//2:
        #print(visited)
        start=0
        link=0
        for i in range(N):
            if visited[i]:
                for j in range(N):
                    if visited[j]:
                        start+=abilities[i][j]
            else:
                for j in range(N):
                    if not visited[j]:
                        link+=abilities[i][j]
        #print(start,link)                
        ans=min(ans,abs(start-link))           
        return
    else:
        for i in range(end,N):
            if not visited[i]:
                visited[i]=1
                DFS(i+1)
                visited[i]=0
    

                  
DFS(0)
print(ans)
