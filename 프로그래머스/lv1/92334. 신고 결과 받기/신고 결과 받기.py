def solution(id_list, report, k):
    answer = []
    systemDict={}
    attackedDict={}
    attackedArr=[]
    for id in id_list:
        systemDict[id]=[]
        attackedDict[id]=0
    for alarm in set(report):
        user,attacked=alarm.split(' ')
        systemDict[user].append(attacked)
        attackedDict[attacked]+=1
    for key in attackedDict:
        if attackedDict[key]>=k:
            attackedArr.append(key)
    
    for key in systemDict:
        answer.append(len(set(systemDict[key])&set(attackedArr)))
    return answer
            
           
