import sys
input=sys.stdin.readline
sudoku=[list(map(int,input().split())) for _ in range(9)]

nums=[1,2,3,4,5,6,7,8,9]
visited=[0]*(9)
checkPoints=[]

def checkCol(x,num):
    global sudoku
    for j in range(9):
        if sudoku[j][x]==num:
            return False
    return True
            
    
def checkRow(y,num):
    global sudoku
    for j in range(9):
        if sudoku[y][j]==num:
            return False
    return True
    
def check3X3(y,x,num):
    global sudoku
    y1=(y//3)*3
    x1=(x//3)*3
    for i in range(y1,y1+3):
        for j in range(x1,x1+3):
            if sudoku[i][j]==num:
                return False             
              
    return True
    
           
            

def DFS(depth):
    global sudoku
    if depth==len(checkPoints):
        for i in range(9):
            print(*sudoku[i])       
        sys.exit(0)
    else:
        for num in range(1,10):
            [y,x]=checkPoints[depth]
            if checkCol(x,num) and checkRow(y,num) and check3X3(y,x,num):
                sudoku[y][x]=num
                DFS(depth+1)
                sudoku[y][x]=0
            
    
for i in range(9):
    for j in range(9):
        if sudoku[i][j]==0:
            checkPoints.append([i,j])
            
DFS(0)            