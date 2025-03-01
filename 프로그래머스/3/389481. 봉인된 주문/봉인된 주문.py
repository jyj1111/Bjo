def solution(n, bans):
    answer = ''
    target=n
    orders=[]
    
    for st in bans:
        num=0
        for i in range(len(st)):
            num*=26
            num+=ord(st[i])-96
            
        orders.append(num)
        
    orders.sort()

    for num in orders:
        if num<=target:
            target+=1
         

    while target>0:
        answer+=chr(((target-1)%26)+97)
        if target%26==0:
            target-=1
        target=target//26


    
    return answer[::-1]
            
        
    