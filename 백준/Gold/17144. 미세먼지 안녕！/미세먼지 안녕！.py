"""
1. 미세먼지가 동시에 확산된다.->4방향으로 확산양:A//5  남은양: A-(확산개수)*A//5
2. 위쪽 공기청정기 반시계방향  아래쪽 공기청정기 시계방향
3. 바람-> 바람의 방향으로 모두 한칸씩 이동
4. 공기청정기로 들어간 미세먼지는 모두 정화된다.
"""
import sys,copy
input=sys.stdin.readline
di=[-1,0,1,0]
dj=[0,1,0,-1]
R,C,T=map(int,input().split()) #6 ≤ R, C ≤ 50, 1 ≤ T ≤ 1,000

graph=[list(map(int,input().split())) for _ in range(R)]

def diffusion():
    global graph,graph1
    for i in range(R):
        for j in range(C):
            if graph1[i][j]>0:
                amount=graph1[i][j]//5#미세먼지가 동시에 확산되기에 복사배열로 확산 계산
                for k in range(4):
                    i1=i+di[k]
                    j1=j+dj[k]
                    if i1<0 or i1>=R:
                        continue
                    if j1<0 or j1>=C:
                        continue
                    if graph1[i1][j1]==-1:
                        continue
                    graph[i1][j1]+=amount
                    graph[i][j]-=amount
    

def cleanUp(cleanerY):
    global graph,graph1
    graph[cleanerY][1]=0
    for i in range(1,C-1):
        graph[cleanerY][i+1]=graph1[cleanerY][i]
    for i in range(cleanerY,0,-1):
        graph[i-1][C-1]=graph1[i][C-1]
    for i in range(C-1,0,-1):
        graph[0][i-1]=graph1[0][i]
    for i in range(cleanerY):
        graph[i+1][0]=graph1[i][0]
    graph[cleanerY][0]=-1

def cleanDown(cleanerY):
    global graph,graph1
    graph[cleanerY+1][1]=0
    for i in range(1,C-1):
        graph[cleanerY+1][i+1]=graph1[cleanerY+1][i]
    for i in range(cleanerY+1,R-1):
        graph[i+1][C-1]=graph1[i][C-1]
    for i in range(C-1,0,-1):
        graph[R-1][i-1]=graph1[R-1][i]
    for i in range(R-1,cleanerY+1,-1):
        graph[i-1][0]=graph1[i][0]
    graph[cleanerY+1][0]=-1

cleanerY=0
for i in range(2,R-2):
    if graph[i][0]==-1:
        cleanerY=i
        break
    
for t in range(T):
    graph1=copy.deepcopy(graph)#미세먼지가 동시에 확산되기에 필요한 복사배열
    diffusion()
    graph1=copy.deepcopy(graph)
    #print(graph)                
    cleanUp(cleanerY)
    #print(graph)
    cleanDown(cleanerY)
    #print(graph)

hap=0
for i in range(R):
    hap+=sum(graph[i])
print(hap+2)