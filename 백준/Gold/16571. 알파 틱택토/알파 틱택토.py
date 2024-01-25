import sys
input=sys.stdin.readline

graph=[list(map(int,input().split())) for _ in range(3)]

def win(before):
    global graph
    
    for i in range(3):
        if graph[i][0]==before and graph[i][0]==graph[i][1]==graph[i][2]:
            return True
        if graph[0][i]==before and graph[0][i]==graph[1][i]==graph[2][i]:
            return True
    if graph[0][0]==before and graph[0][0]==graph[1][1]==graph[2][2]:
        return True
    if graph[0][2]==before and graph[0][2]==graph[1][1]==graph[2][0]:
        return True
    return False


def backtracking(turn):
    global points
    global graph
    before=3-turn
    w=win(before)
    if w:
        return -1
    else:
        tmp=2
        for i,j in points:
            if graph[i][j]==0:
                graph[i][j]=turn
                tmp=min(tmp,backtracking(3-turn))
                graph[i][j]=0

        if tmp==2 or tmp==0:
            return 0
        else:
            return -tmp
 
    
            
    
cnt=0
points=[]
for i in range(3):
    for j in range(3):
        if graph[i][j]>0:
            cnt+=1
        else:
            points.append((i,j))

turn=0
if cnt%2==0:
    turn=1
else:
    turn=2

ans=backtracking(turn)

if ans==0:
    print('D')
elif ans==1:
    print('W')
else:
    print('L')