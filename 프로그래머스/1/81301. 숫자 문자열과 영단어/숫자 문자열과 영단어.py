from collections import defaultdict
numkeys=['zero','one','two','three','four','five','six','seven','eight','nine']
def solution(s):
    ans='' 
    dic=defaultdict(str)
    for i in range(10):
        dic[numkeys[i]]=str(i)
    tmp=''    
    for i in range(len(s)):
        if s[i].isdigit():
            ans+=s[i]
        else:
            tmp+=s[i]
            if tmp in dic:
                ans+=dic[tmp]
                tmp=''
      
    
    return int(ans)