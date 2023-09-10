import sys
input=sys.stdin.readline
from itertools import combinations

n,k=map(int,input().split())## n은 50이하 k는 26이하

cnt=0
wordArr=[]
basicCh={'a','n','t','i','c'}##anta.tica에 들어있는 문자들
ch=set() ##anta.tica에 들어있지 않는  문자들

for i in range(n):
    word=input().rstrip('\n')
    wordSet=set(word[4:-4])-basicCh
    if len(wordSet)>k-5:
        continue
    elif len(wordSet)==0:
        cnt+=1
    else:
        ch.update(wordSet)
        wordArr.append(wordSet)   

        
if k<5:
    print(0)
elif len(wordArr)==0:
    print(cnt)
elif len(ch)<=k-5:
    print(cnt+len(wordArr))
else:
    cnt1=0
    for combi in combinations(ch,k-5):
        num=0
        combiSet=set(combi)
        for wordSet in wordArr:
            
            if wordSet<=combiSet:## 부분집합 여부
                num+=1
        cnt1=max(cnt1,num)

    print(cnt+cnt1)
