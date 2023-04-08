from itertools import combinations
def slope(arr):
    x1,y1=arr[0]
    x2,y2=arr[1]
    return (y2-y1)/(x2-x1)
    
def solution(dots):
    arr=list(combinations(dots,2))
    for i in range(3):
        
        if slope(list(arr[i]))==slope(list(arr[5-i])):
            return 1
    return 0
        
    
        