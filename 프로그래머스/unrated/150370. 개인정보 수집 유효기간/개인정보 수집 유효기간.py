def dateToNum(date):
        year,month,day=map(int,date.split('.'))
        return 12*28*year+28*month+day
    
def solution(today, terms, privacies):
    answer = []    
    numToday=dateToNum(today)
    for i in range(len(privacies)):
        date,promise=privacies[i].split(' ')
        for term in terms:
            ch,num=term.split(' ')
            if promise==ch and dateToNum(date)+int(num)*28<=numToday:
                answer.append(i+1)
                    
    return answer