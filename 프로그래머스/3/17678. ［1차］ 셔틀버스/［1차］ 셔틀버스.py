from collections import defaultdict,deque

def dateToNum(s):
    hour,minute=map(int,s.split(':'))
    return 60*hour+minute

def numToDate(num):
    hour,minute=str(num//60),str(num%60)
    return hour.zfill(2)+":"+minute.zfill(2)
    

def solution(n, t, m, timetable):
    answer = ''
    waitTime=deque(sorted([dateToNum(time) for time in timetable]))
    busStart,busEnd=dateToNum('09:00'),dateToNum('09:00')+(n*t)
    busSizeTimeTable=defaultdict(list)
    for ArriveTime in range(busStart,busEnd,t):
        while len(busSizeTimeTable[ArriveTime])<m and waitTime and waitTime[0]<=ArriveTime:
            busSizeTimeTable[ArriveTime].append(waitTime.popleft())
            
    if len(busSizeTimeTable[busEnd-t])<m:
        answer=numToDate(busEnd-t)    
    elif len(busSizeTimeTable[busEnd-t])==m:
        answer=numToDate(max(busSizeTimeTable[busEnd-t])-1)
        
    return answer
