digits = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
              
def numeral(num, n):
    res = ''
    while num > 0:
        num,mod=divmod(num, n)
        res=digits[mod]+res
    return res

def solution(n, t, m, p):
    answer= ''
    tmp='0'
    num=1
    while True:
        tmp+=numeral(num, n)
        if len(tmp)>m*t:
            break
        num+=1
    
    for i in range(p-1,m*t,m):
        answer+=tmp[i]
       
    
    return answer
