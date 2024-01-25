
def solution(edges):
    answer = [0,0,0,0]
    maxNode=0
    center=0
    for a,b in edges:
        maxNode=max(maxNode,max(a,b))
        
    graph=[[[] for _ in range(2)] for _ in range(maxNode+1)]
    
    for a,b in edges:
        graph[a][0].append(b)
        graph[b][1].append(a)
            
    for i in range(1,maxNode+1):
        outList,inList=graph[i]
        if len(outList)>=2 and len(inList)==0: ## 생성 정점
            answer[0]=i
            center=i
        if len(outList)>=2 and len(inList)>=2:## 8자 모양
            answer[3]+=1
        elif len(outList)==0 and len(inList)>0: ## 막대모양
            answer[2]+=1

    answer[1]=len(graph[center][0])-(answer[2]+answer[3]) ## 도넛모양

    return answer