from collections import deque,defaultdict
def solution(gems):
    gemsDic=set(gems)#보석의 종류
    n,m=len(gems),len(gemsDic)
    answers=[]
    l,r=0,0
    dic=defaultdict(int)
    kind=0
    cnt=0
    while l<=r and cnt<2*n:
        if kind==m:
            
            answers.append([l+1,r])
            if dic[gems[l]]==1:
                kind-=1
            dic[gems[l]]-=1
            l+=1
        elif kind<m and r<n:
            if dic[gems[r]]==0:
                kind+=1
            dic[gems[r]]+=1
            r+=1
        cnt+=1
    
    answers.sort(key=lambda x:(x[1]-x[0],x[0]))
    return answers[0]
            

    
            
    