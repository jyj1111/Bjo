import sys
input=sys.stdin.readline

n,m=map(int,input().split())#n,m<=500
boards=[list(map(int,input().split())) for _ in range(n)]

directions=[[(0,0),(0,1),(0,2),(0,3)],[(0,0),(0,1),(1,0),(1,1)],[(0,0),(1,0),(2,0),(2,1)],[(0,0),(1,0),(1,1),(2,1)],[(0,0),(0,1),(1,1),(0,2)]]

def Tetromino(y,x,direction):
    hap=0
    for i,j in [(1,1),(-90,90),(-1,-1),(90,-90),(1,-1),(-1,1),(90,90),(-90,-90)]:
        hap1=0
        for k,t in direction:
            #print(i,j)
            #print(k,t)->
            if i==90 and j==-90:
                y1=y-t
                x1=x+k 

            elif i==90 and j==90:
                y1=y+t
                x1=x+k
            elif i==-90 and j==90:
                y1=y+t
                x1=x-k
            elif i==-90 and j==-90:
                y1=y-t
                x1=x-k 
                
            else:
                y1=y+k*i
                x1=x+t*j
            #print(y1,x1)    
            if y1>=n or y1<0 or  x1>=m or x1<0:
                hap1=0
                break
            
            hap1+=boards[y1][x1]
        #print(y,x,i,j,hap1)
        hap=max(hap,hap1)
    return hap    



ans=0

for i in range(n):
    for j in range(m):
        for direction in directions:
            ans=max(ans,Tetromino(i,j,direction))
       
print(ans)
        