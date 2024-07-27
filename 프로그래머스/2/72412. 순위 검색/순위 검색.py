from collections import defaultdict
from bisect import bisect_left

def solution(info, query):
    dic=defaultdict(list)
    answer = []
    for inf in info:
        lang,pos,career,food,point=inf.split(' ')
        dic[lang+pos+career+food].append(int(point))
        dic[lang+pos+career+food].sort()

    for message in query:
        lang,pos,career,foodpoint=message.split(" and ")
        food,point=foodpoint.split(" ")
        langGroup,posGroup,careerGroup,foodGroup=[],[],[],[]
        if lang=='-':
            langGroup+=['java','python','cpp']
        else:
            langGroup+=[lang]
        if pos=='-':
            posGroup+=['backend','frontend']
        else:
            posGroup+=[pos]
        if career=='-':
            careerGroup+=['junior','senior']
        else:
            careerGroup+=[career]
        if food=='-':
            foodGroup+=['chicken','pizza']
        else:
            foodGroup+=[food]
        
        cnt=0
        
        for l in langGroup:
            for p in posGroup:
                for c in careerGroup:
                    for f in foodGroup:
                        idx=bisect_left(dic[l+p+c+f],int(point))
                        cnt+=len(dic[l+p+c+f])-idx
                                    
        answer.append(cnt)                        
                        
                            
                            
        
        
    return answer