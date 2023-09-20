import sys
input=sys.stdin.readline
N=int(input()) ## 1 ≤ N ≤ 8
eggs=[list(map(int,input().split())) for _ in range(N)]

cnt=0

def DFS(idx,cut):
    global cnt
    
    #print(idx,cut)
    if idx==N:
       cnt=max(cnt,cut)
       return
    if eggs[idx][0]<=0:
        DFS(idx+1,cut)
    else:
        flag=False
        
        for i in range(N):
            if i==idx or eggs[i][0]<=0:
                continue
            flag=True
            eggs[idx][0]-=eggs[i][1]
            eggs[i][0]-=eggs[idx][1]
            DFS(idx+1,cut+int(eggs[idx][0]<=0)+int(eggs[i][0]<=0))
            eggs[idx][0]+=eggs[i][1]
            eggs[i][0]+=eggs[idx][1]

        if not flag:
            DFS(idx+1,cut)
 

DFS(0,0)
print(cnt)