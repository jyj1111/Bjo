def kinary(n,k):
    ans=''
    while n>0:
        n,r=divmod(n,k)
        ans+=str(r)
    return ans[::-1]  
def prime(num):
    if num<=1:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True
def solution(n, k):
    answer = 0
    for num in kinary(n,k).split('0'):
        if num and prime(int(num)):
            answer+=1
    return answer