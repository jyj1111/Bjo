from collections import deque
def solution(rc, operations):
    firstDeque=deque([r[0] for r in rc])
    midDeque=deque([deque(r[1:-1]) for r in rc])
    lastDeque=deque([r[-1] for r in rc])
    for operation in operations:
        if operation=='ShiftRow':
            firstDeque.appendleft(firstDeque.pop())
            midDeque.appendleft(midDeque.pop())
            lastDeque.appendleft(lastDeque.pop())
        elif operation=='Rotate':
            midDeque[0].appendleft(firstDeque.popleft())
            lastDeque.appendleft(midDeque[0].pop())
            midDeque[-1].append(lastDeque.pop())
            firstDeque.append(midDeque[-1].popleft())
            
    return [[firstDeque[i]]+list(midDeque[i])+[lastDeque[i]] for i in range(len(rc))] 
        