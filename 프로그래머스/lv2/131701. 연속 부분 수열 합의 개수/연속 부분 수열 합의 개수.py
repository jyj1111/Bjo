def solution(elements):
    answer = set();
    arr=elements+elements
    for i in range(len(elements)):
        for j in range(1,len(elements)+1):
            
            answer.add(sum(arr[i:i+j]))
    return len(answer)