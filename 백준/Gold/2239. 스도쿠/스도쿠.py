import sys
input=sys.stdin.readline

sudoku=[list(map(int,input().rstrip('\n'))) for _ in range(9)]
arr=[]

def check3X3(num,i,j):
    global sudoku
    i1=(i//3)*3
    j1=(j//3)*3
    for y1 in range(i1,i1+3):
        for x1 in range(j1,j1+3):
            if sudoku[y1][x1]==num:
                return False         
    return True

def checkCol(num,j):
    global sudoku
    for i in range(9):
        if sudoku[i][j]==num:
            return False
    return True

def checkRow(num,i):
    global sudoku
    for j in range(9):
        if sudoku[i][j]==num:
            return False
    return True
    

def DFS(idx):
    global sudoku
    if idx==len(arr):
        for i in range(9):
            print(''.join(map(str,sudoku[i])))
        sys.exit(0)
            

    else:
        for num in range(1,10):
            [i,j]=arr[idx]
            if check3X3(num,i,j) and checkCol(num,j) and checkRow(num,i):
                sudoku[i][j]=num
                DFS(idx+1)
                sudoku[i][j]=0
                        
                
        


for i in range(9):
    for j in range(9):
        if sudoku[i][j]==0:
            arr.append([i,j])
            
DFS(0)
