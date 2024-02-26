from collections import defaultdict
from itertools import combinations

def solution(friends, gifts):
    answer = 0
    giveDic=defaultdict(int)
    numDic=defaultdict(int)
    num1Dic=defaultdict(int)
    
    for gift in gifts: # 10000
        giver,receiver=gift.split(' ')
        giveDic[(giver,receiver)]+=1
        numDic[giver]+=1
        numDic[receiver]-=1
    
    for user,friend in combinations(friends,2):
        num1=giveDic[(user,friend)]
        num2=giveDic[(friend,user)]
        if num1>num2:
            num1Dic[user]+=1
        elif num1<num2:
            num1Dic[friend]+=1
        else:
            if numDic[user]>numDic[friend]:
                num1Dic[user]+=1
            elif numDic[user]<numDic[friend]:
                num1Dic[friend]+=1

    for key,value in num1Dic.items():
        answer=max(answer,value)
     
        
    return answer