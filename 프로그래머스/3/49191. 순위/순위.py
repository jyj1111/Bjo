from collections import deque,defaultdict

def solution(n, results):
    answer = 0
    graph=[[[],[]] for _ in range(n+1)]
    
    queue=deque()
    indegree=[0]*(n+1)
    for win,lose in results:
        graph[win][0].append(lose)
        graph[lose][1].append(win)
        indegree[lose]+=1
    print(graph)
    """
    for i in range(1,n+1):
        if indegree[i]==0:
            queue.append(i)

    ranks=[]
    while queue:
        n=queue.popleft()
        ranks.append(n)
        for j in graph[n]:
            indegree[j]-=1
            if indegree[j]==0:
                queue.append(j)
    print(graph)
    print(ranks)    
    """    
    return answer