
def distance(x1,y1,x2,y2):
    return abs(x1-x2)+abs(y1-y2)
def isValid(x1,y1,x2,y2,place):
    if distance(x1,y1,x2,y2)>2:
        return True    
    elif distance(x1,y1,x2,y2)==2:
        if x1==x2 and place[x1][y1+1]=='X': #세로축 평행
            return True        
        elif y1==y2 and place[x1+1][y1]=='X':# 가로축 평행
            return True
        elif x1!=x2 and y1!=y2 and place[x1][y2]=='X' and place[x2][y1]=='X':#대각선
            return True
        return False
    else:
        return False
    
def solution(places):
    answer = []
    for place in places:
        peoples=[]
        for i in range(5):
            for j in range(5):
                if place[i][j]=='P':
                    peoples.append((i,j))
        n=len(peoples)
        valid=True
        for i in range(n-1):
            for j in range(i+1,n):
                x1,y1=peoples[i]
                x2,y2=peoples[j]
                if not isValid(x1,y1,x2,y2,place):
                    valid=False
                    break
            if not valid:
                break
        if valid:
            answer.append(1)
        else:
            answer.append(0)
                   
                
    return answer