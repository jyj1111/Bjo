"""
사전순: d(+,0),l(0,-),r(0,+),u(-,0)
"""
def solution(n, m, x, y, r, c, k):
    answer = ''
    moveX=x
    moveY=y
    dis=k
    if (dis- abs(r - moveX)-abs(c - moveY))%2==1 or abs(r - moveX)+abs(c - moveY)>dis:
        return "impossible"
    while dis- (abs(r - moveX)+abs(c - moveY))>0:
        if 1<=moveX+1<=n:
            moveX+=1
            answer+='d'
        elif 1<=moveY-1<=m:
            moveY-=1
            answer+='l'
        elif 1<=moveY+1<=m:
            moveY+=1
            answer+='r'
        elif 1<=moveX-1<=n:
            moveX-=1
            answer+='u'
        dis-=1
    if r-moveX >= 0 and c-moveY >= 0:
        answer+='d'*abs(r-moveX)
        answer+='r'*abs(c-moveY)
    elif r-moveX >= 0 and c-moveY < 0:
        answer+='d'*abs(r-moveX)
        answer+='l'*abs(c-moveY)
    elif r-moveX < 0 and c-moveY >= 0:
        answer+='r'*abs(c-moveY)
        answer+='u'*abs(r-moveX)
    elif r-moveX < 0 and c-moveY < 0:
        answer+='l'*abs(c-moveY)
        answer+='u'*abs(r-moveX)
    return answer