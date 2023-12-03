from collections import deque,defaultdict

def solution(n, results):
    answer = 0
    winDic = defaultdict(set)    
    loseDic = defaultdict(set)   
    for winner,loser in results:        
        winDic[loser].add(winner)
        loseDic[winner].add(loser)
    for i in range(1,n+1):         
        for winner in winDic[i]:                    
            loseDic[winner].update(loseDic[i])
        for loser in loseDic[i]:                    
            winDic[loser].update(winDic[i])
    
    for i in range(1,n+1):
        if len(winDic[i])+len(loseDic[i]) == n-1:   
            answer+=1
        
    return answer