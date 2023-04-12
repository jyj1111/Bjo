def solution(board, skill):
    imos=[[0]*(len(board[0])+1) for _ in range(len(board)+1)]
    for s in skill:
        type,x1,y1,x2,y2,degree=s;
        if type==1:
            degree=-degree
        imos[x1][y1]+=degree
        imos[x1][y2+1]-=degree
        imos[x2+1][y1]-=degree
        imos[x2+1][y2+1]+=degree
        
    for i in range(len(imos)):
        for j in range(1,len(imos[0])):
            imos[i][j]+=imos[i][j-1]
                
    for i in range(len(imos[0])):
        for j in range(1,len(imos)):
            imos[j][i]+=imos[j-1][i]    
         
    answer = 0      
    for i in range(0,len(board)):
        for j in range(0, len(board[0])):
            board[i][j]+=imos[i][j]
            if board[i][j]>0:
                answer+=1
    return answer