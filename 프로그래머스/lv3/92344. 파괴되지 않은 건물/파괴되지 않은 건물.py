def solution(board, skill):
    for s in skill:
        type,x1,y1,x2,y2,degree=s;
        if type==1:
            degree=-degree
        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                board[i][j]+=degree
           
    answer = 0      
    for i in range(0,len(board)):
        for j in range(0, len(board[0])):
            if board[i][j]>0:
                answer+=1
    return answer