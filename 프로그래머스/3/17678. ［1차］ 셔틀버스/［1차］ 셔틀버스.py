
def dateToNum(time):
    hour,minute=time.split(':')
    return 60*int(hour)+int(minute)
def numToDate(num):
    hour=num//60
    minute=num%60
    return str(hour).zfill(2)+":"+str(minute).zfill(2)
def solution(n, t, m, timetable):
    answer =0
    crewTimes=[]
    for time in timetable:
        crewTimes.append(dateToNum(time))
    crewTimes.sort()
    busTimes=[]
    for i in range(n):
        busTimes.append(540+i*t)
    
    for busTime in busTimes:
        cnt=0
        busridingCrewTimes=[]
        while crewTimes:
            if cnt<m and crewTimes[0]<=busTime:
                cnt+=1
                busridingCrewTimes.append(crewTimes.pop(0))
            else:
                break

        if cnt<m:
            answer=busTime
        else:
            answer=busridingCrewTimes[m-1]-1
            
        
    return numToDate(answer)