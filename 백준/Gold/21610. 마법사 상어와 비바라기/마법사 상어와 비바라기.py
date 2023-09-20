import sys,copy
N,M=map(int,input().split()) ## 2 ≤ N ≤ 50, 1 ≤ M ≤ 100
A=[list(map(int,input().split())) for _ in range(N)] ##0 ≤ A[r][c] ≤ 100

dy=[0,0,-1,-1,-1,0,1,1,1]  #방향
dx=[0,-1,-1,0,1,1,1,0,-1]


clouds=[[N-2,0],[N-2,1],[N-1,0],[N-1,1]]

for i in range(M):
    #print(A)        
    di,si=map(int,input().split()) ##1 ≤ di ≤ 8, 1 ≤ si ≤ 50
    
    visited=[[0]*(N) for _ in range(N)] # 구름 방문 여부 배열
    
    for cloud in clouds: # 구름 di,si만큼 이동
        y,x=cloud
        y1=(y+dy[di]*si)%N
        x1=(x+dx[di]*si)%N
        cloud[0]=y1
        cloud[1]=x1
        visited[y1][x1]=1
    
    for cloud in clouds:# 칸이 1씩 증가
        y,x=cloud
        A[y][x]+=1
       

    for cloud in clouds:# 대각선 방향으로 물이 있는 만큼 칸수 증가
        y,x=cloud
        cnt=0
        for d in range(2,9,2):
            y1=y+dy[d]
            x1=x+dx[d]
            if 0<=y1<N and 0<=x1<N:# 이동과 다르게 경계를 넘어갈 수 없음
                if A[y1][x1]>0:
                    cnt+=1
        
        A[y][x]+=cnt
     

    newClouds=[] # 새로운 구름 

    for j in range(N): #칸의 값이 2이상인 곳에만 구름이 생기고 구름이 있는 칸에 2만큼 줄어듬
        for k in range(N):
                  
            if A[j][k]>=2 and not visited[j][k]:
                newClouds.append([j,k])
                A[j][k]-=2

    clouds=copy.deepcopy(newClouds)
    
hap=0
for i in range(N):
    hap+=sum(A[i])

print(hap) # 바구니 물의 총 합