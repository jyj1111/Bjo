
from collections import deque
def solution(queue1, queue2):
    answer =0
    q1=deque(queue1)
    q2=deque(queue2)
    limit=len(q1)*3
    s1=sum(q1)
    s2=sum(q2)
    while answer<limit:
        if s1==s2:
            return answer
        elif s1>s2:
            tmp=q1.popleft()
            q2.append(tmp)
            s1-=tmp
            s2+=tmp
        else:
            tmp=q2.popleft()
            q1.append(tmp)
            s1+=tmp
            s2-=tmp
        answer+=1
    return -1
        
    
            
    