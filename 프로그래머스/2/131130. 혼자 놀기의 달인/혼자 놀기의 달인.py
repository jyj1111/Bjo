def solution(cards):
    answer = []
    visited=[False]*(len(cards))
    for i in range(len(cards)):
        cnt=0
        while not visited[i]:
            visited[i]=True
            i=cards[i]-1
            cnt+=1
        answer.append(cnt)
    answer.sort()        
    return answer[-1]*answer[-2]