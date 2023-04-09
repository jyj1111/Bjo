from itertools import permutations
def solution(babbling):
    ans=0
    arr=["aya","ye","woo","ma"];
    words=[]
    for i in range(1,5):
        for word_list in list(permutations(arr,i)):
            words.append(''.join(word_list));
    for word in babbling:
        if word in words:
            ans+=1
      
    return ans
        
            
            
        
        
    
                
   