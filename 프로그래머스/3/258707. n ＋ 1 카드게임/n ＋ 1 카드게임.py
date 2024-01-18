from collections import defaultdict

def find(arr1,arr2,num):

    dic=defaultdict(int)
    for num1 in arr1:
        dic[num+1-num1]=num1
    for num2 in arr2:
        if num2 in dic.keys():
            arr1.remove(num+1-num2)
            arr2.remove(num2)
            return True
    return False

def solution(coin, cards):
    answer = 1
    num=len(cards)
    round=num//3
    initialCards=cards[:round]
    coinNum=coin
    possibles=[]
    while round<(num-1) and coinNum>=0:
        possibles+=cards[round:round+2]
        #print(initialCards,possibles)
        if find(initialCards,initialCards,num):
            round+=2
            answer+=1
        elif coinNum>=1 and find(initialCards,possibles,num):
            round+=2
            coinNum-=1
            answer+=1
        elif coinNum>=2 and find(possibles,possibles,num):
            round+=2
            coinNum-=2
            answer+=1
        else:
            break
   
    
    return answer