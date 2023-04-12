import math
def timetoNum(time):
    hour,minute=time.split(':')
    return int(hour)*60+int(minute)
def solution(fees, records):
    answer = []
    times={}
    for record in records:
        time, car, state=record.split(' ')
        times[car]=0

    for record in records:
        time, car, state=record.split(' ')
        if state=='IN':
            times[car]-=timetoNum(time);
        else:
            times[car]+=timetoNum(time);
    arr=sorted(times.items())
    parkingtime=[] 
    for i in range(len(arr)):
        arr1=list(arr[i])
        if arr1[1]<=0:
            arr1[1]+=timetoNum("23:59")
        parkingtime.append(arr1[1])
    basetime,baseprice,basetimeslice,basepriceslice=fees
    for t in parkingtime:
        time1=max((t-basetime),0)
        print(time1)
        answer.append(baseprice+((math.ceil(time1/basetimeslice))*basepriceslice))
    return answer