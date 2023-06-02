from collections import defaultdict
def solution(survey, choices):
    answer = ''
    point=[-1,3,2,1,0,1,2,3]
    type=defaultdict(int)
    for i in range(len(choices)):
        if choices[i]>4:
            type[survey[i][1]]+=point[choices[i]]           
        elif choices[i]<4:
            type[survey[i][0]]+=point[choices[i]] 
    for personality in ["RT","CF","JM","AN"]:
        if type[personality[0]]>=type[personality[1]]:
            answer+=personality[0]
        else:
            answer+=personality[1]
        
    return answer