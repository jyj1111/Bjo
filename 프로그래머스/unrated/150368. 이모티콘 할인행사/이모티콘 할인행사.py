from itertools import product
def solution(users, emoticons):
    answer = [0,0]
    discount=[10,20,30,40]
    n,m=len(users),len(emoticons)
    cases=list(product(discount,repeat=m))
    answer_list=[]
    for case in cases:
        cnt=0
        totalPrice=0
        for user in users:
            price=0
            for i in range(m):
                if user[0]<=case[i]:
                    price+=emoticons[i]-(emoticons[i]*case[i]/100)
            if price>=user[1]:
                cnt+=1
            else:
                totalPrice+=price
        answer[0]=max(answer[0],cnt)    
        answer_list.append([cnt,totalPrice])
        
    for arr in answer_list:
        if arr[0]==answer[0]:
            answer[1]=max(answer[1],arr[1])
            
    return answer
                    
                
            
            