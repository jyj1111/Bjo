#7->111 42->0101010 5->101
# 63->0111111 111->1101111  95->1011111
# 0001000
import math
def high(bin):
    l=len(bin)
    return int(math.log(l,2))+1

def dummyBinary(num):
    bin=''
    while num>0:
        bin+=str(num%2)
        num=num//2
    bin=bin[::-1]
    h=high(bin)
    l=len(bin)
    return (2**h-1-l)*'0'+bin
    
def check(bin):
    if len(bin)==1:
        return True
    else:
        mid=len(bin)//2
        if bin[mid]=='0':
            if bin=='0'*(len(bin)):
                return True
            else:
                return False
        else:
            return check(bin[:mid]) and check(bin[mid+1:])             
 
    
    

def solution(numbers):
    answer = []
    for number in numbers:
        bin=dummyBinary(number)
        if check(bin):
            answer.append(1)
        else:
            answer.append(0)
    
    return answer