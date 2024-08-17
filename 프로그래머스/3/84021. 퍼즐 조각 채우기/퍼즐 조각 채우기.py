from collections import deque
def in_bound(y1,x1,y,x):
    return 0<=y1<y and 0<=x1<x
def rotate(arr):
    return list(map(list,zip(*arr[::-1])))
def find_neighbor(board,flag):
    arr=[]
    y,x=len(board),len(board[0])
    visited=[[False]*(x) for _ in range(y)]
    for i in range(y):
        for j in range(x):
            if not visited[i][j] and board[i][j]==flag:
                visited[i][j]=True
                lst=[(i,j)]
                queue=deque([(i,j)])
                while queue:
                    y1,x1=queue.popleft()
                    for dy,dx in [(-1,0),(0,1),(1,0),(0,-1)]:
                        y2,x2=y1+dy,x1+dx
                        if in_bound(y2,x2,y,x) and not visited[y2][x2] and board[y2][x2]==flag:
                            visited[y2][x2]=True
                            lst.append((y2,x2))
                            queue.append((y2,x2))
                            
                arr.append(lst)
    return arr

def new_piece(piece):
    y_list,x_list=map(list,zip(*piece))
    start_y,max_y,start_x,max_x=min(y_list),max(y_list),min(x_list),max(x_list)
    new_piece=[[0]*(max_x-start_x+1) for _ in range(max_y-start_y+1)]
    for i,j in piece:
        new_piece[i-start_y][j-start_x]=1
    return new_piece

def solution(game_board, table):
    answer = 0
    empty_blocks=find_neighbor(game_board,0)
    puzzle_blocks=find_neighbor(table,1)
    for empty_block in empty_blocks:
        new_empty=new_piece(empty_block)
        empty=True
        for puzzle in puzzle_blocks:
            new_puzzle=new_piece(puzzle)
            for i in range(4):
                new_puzzle=rotate(new_puzzle)
                if new_empty==new_puzzle:
                    answer+=len(puzzle)
                    puzzle_blocks.remove(puzzle)
                    empty=False
                    break
            if not empty:
                break
    
    
    
    
    return answer