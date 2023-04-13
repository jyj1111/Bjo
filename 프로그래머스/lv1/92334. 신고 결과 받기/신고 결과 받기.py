def solution(id_list, report, k):
    answer = []
    systemDict={}
    attackedDict={}
    attackedSet=set()
    for id in id_list:
        systemDict[id]=set()
        attackedDict[id]=0
    for alarm in set(report):
        user,attacked=alarm.split(' ')
        systemDict[user].add(attacked)
        attackedDict[attacked]+=1
    for key in attackedDict:
        if attackedDict[key]>=k:
            attackedSet.add(key)
    
    for key in systemDict:
        answer.append(len(systemDict[key]&attackedSet))
    return answer
            
           
