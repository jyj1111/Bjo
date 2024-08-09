from itertools import combinations,product
from collections import defaultdict

def solution(dice):
    answer = []
    n=len(dice)
    maxWin=0
    for combi,idxs in zip(combinations(dice,n//2),combinations(range(1,n+1),n//2)):
        dicA=defaultdict(int)
        dicB=defaultdict(int)
        for compo in product(*combi):
            dicA[sum(compo)]+=1
            
        complement=[x for x in dice if x not in list(combi)]
        for compo in product(*complement):
            dicB[sum(compo)]+=1
        
        win=0
        for key1,value1 in dicA.items():
            for key2,value2 in dicB.items():
                if key1>key2:
                    win+=value1*value2
        
        if win>maxWin:
            maxWin=win
            answer=list(idxs)

 
    return answer