from itertools import combinations_with_replacement
def solution(n, info):
    answer = [-1]
    point=0
    for li in list(combinations_with_replacement(range(11),n)):
        maxpoint=0
        ryan=[0]*11
        for num in list(li):
            ryan[10-num]+=1
        for i in range(len(info)):
            if info[i]==ryan[i]==0:
                continue
            elif info[i]<ryan[i]:
                maxpoint+=10-i
            elif info[i]>=ryan[i]:    
                maxpoint-=10-i
                         
        if maxpoint>point:
            point=maxpoint
            answer=ryan
           
    return answer