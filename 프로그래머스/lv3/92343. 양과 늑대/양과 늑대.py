def solution(info, edges):
    answer=[]
    visited=[0]*(len(info))
    def DFS(sheep,wolf):
        if sheep>wolf:
            answer.append(sheep)
        else:
            return
        
        for edge in edges:
            parent,child=edge
            if visited[parent] and visited[child]==0:
                visited[child]=1
                if info[child]==0:
                    DFS(sheep+1,wolf)
                else:
                    DFS(sheep,wolf+1)
                visited[child]=0
                    
    visited[0]=1
    DFS(1,0)
    return max(answer)
        
        
        
        