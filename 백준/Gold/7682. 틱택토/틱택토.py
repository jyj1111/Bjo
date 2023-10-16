"""
xxx
oox
oox
"""
import sys
input=sys.stdin.readline

clear=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

def winCheck(s):
    xwin=0
    owin=0
    for a1,a2,a3 in clear:
       if s[a1]==s[a2]==s[a3]:
           if s[a1]=='X':
               xwin+=1
           elif s[a1]=='O':
               owin+=1
    return [xwin,owin]
        
                

def validCheck(s):
    a=s.count('X')
    b=s.count('O')
    c=s.count('.')
    
    if c==0 and a==5 and b==4:
        xwin,owin=winCheck(s)
        if owin==0:
            return 'valid'
        
    elif c==1 and a==4 and b==4:
        xwin,owin=winCheck(s)
        if xwin==0 and owin==1:
            return 'valid'

    elif c==2 and a==4 and b==3:
        xwin,owin=winCheck(s)
        if xwin==1 and owin==0:
            return 'valid'

    elif c==3 and a==3 and b==3:
        xwin,owin=winCheck(s)
        if xwin==0 and owin==1:
            return 'valid'

    elif c==4 and a==3 and b==2:
        xwin,owin=winCheck(s)
        if xwin==1 and owin==0:
            return 'valid'

    
    return 'invalid'
        
    

while True:
    tictactoe=input().rstrip('\n')
    if tictactoe=='end':
        break
    print(validCheck(tictactoe))