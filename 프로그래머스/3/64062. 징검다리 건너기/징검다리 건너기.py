def solution(stones, k):
    l=1
    r=200000000
    while l<=r:
        mid=(l+r)//2
        cnt=0
        for stone in stones:
            if stone-mid<0:
                cnt+=1
            else:
                cnt=0
            if cnt==k:
                break
                
        if cnt<k:
            l=mid+1
            answer=mid
        else:
            r=mid-1
    
    return answer