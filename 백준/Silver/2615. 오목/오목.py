import sys
input=sys.stdin.readline
graph=[list(map(int,input().split())) for _ in range(19)]
# 검은:1, 흰:2, 알x: 0

di=[-1,0,1,1] 
dj=[1,1,1,0]

# 방향: 오른쪽 위 대각선, 오른쪽, 오론쪽 아래 대각선, 아래
                    
decide=False

def BFS(i,j):
    global decide
    target=graph[i][j]
    directions=[]
    for k in range(4):
        y=i+di[k]
        x=j+dj[k]
        if 0<=y<19 and 0<=x<19 and graph[y][x]==target:
            directions.append([di[k],dj[k]])
        
    for dy,dx in directions:
        y=i
        x=j
        cnt=0
        
        while 0<=y<19 and 0<=x<19 and graph[y][x]==target:
            
            cnt+=1
            #print(y,x,cnt)
            if cnt==5:
                if 0<=i-dy<19 and 0<=j-dx<19 and graph[i-dy][j-dx]==target:
                    cnt=6
                    break
                    
                    
            y=y+dy
            x=x+dx        
                    
        
        if cnt==5:
            print(target)
            print(i+1,j+1)
            decide=True
            break
            



for i in range(19):
    for j in range(19):
        if graph[i][j]>0:
            BFS(i,j)

if not decide:
    print(0)