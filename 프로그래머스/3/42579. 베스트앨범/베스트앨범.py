from collections import defaultdict
from heapq import heappush,heappop
def solution(genres, plays):
    answer = []
    genrePlays=defaultdict(list)
    genrehap=defaultdict(int)
    for idx,(genre,play) in enumerate(zip(genres,plays)):
        genrehap[genre]+=play
        heappush(genrePlays[genre],(-play,idx))
    
    for genre,hap in sorted(genrehap.items(), key=lambda x:x[1], reverse=True):
        n=len(genrePlays[genre])
        for i in range(min(2,n)):
            play,idx=heappop(genrePlays[genre])
            answer.append(idx)
 
    return answer