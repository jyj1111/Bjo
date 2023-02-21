from collections import deque

def dfs(graph, visited, start):
    
    visited[start-1]=1   
    print(start,end=' ')
    for i in range(len(visited)):       
        if (graph[start-1][i]==1) and (visited[i]==0):
            dfs(graph,visited,i+1)      
                
def bfs(graph, visited, start):
    queue=deque()
    queue.append(start-1)
    visited[start-1]=1
    while queue:
        visit=queue.popleft()
        
        print(visit+1,end=' ')
        
        for i in range(len(visited)):
            if graph[visit][i]==1 and visited[i]==0:
                visited[i]=1
                queue.append(i)
                    
        
    
n,e,start=map(int,input().split())
graph=[[0]*n for _ in range(n)]
visited=[0]*n
for i in range(e):
    a,b=map(int,input().split())
    graph[a-1][b-1]= graph[b-1][a-1]=1
     
    
dfs(graph, visited, start)
print('')
visited=[0]*n 
bfs(graph, visited, start)          