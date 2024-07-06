def timeToNum(str):
    h,m,s=map(int,str.split(':'))
    return h*3600+m*60+s

def numToTime(num):
    h=num//3600
    num=num%3600
    m=num//60
    s=num%60
    return str(h).zfill(2)+":"+str(m).zfill(2)+":"+str(s).zfill(2)

def solution(play_time, adv_time, logs):
    adv,play=timeToNum(adv_time),timeToNum(play_time)
    times=[0]*(play+1)
    for log in logs:
        s,e=map(timeToNum,log.split('-'))     
        times[s]+=1
        times[e]-=1
    for i in range(1,play+1):
        times[i]+=times[i-1]
    
    maxplays=sum(times[:adv])
    curplays=maxplays
    maxtime=0
    for i in range(1,play-adv+1):
        curplays+=times[i+adv-1]-times[i-1]
        if curplays>maxplays:
            maxplays=curplays
            maxtime=i
       
    return numToTime(maxtime)