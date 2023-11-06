import sys
input=sys.stdin.readline
N,M=map(int,input().split())# 2 <= N <= 5, 1<=M=<100,000,000,000
Matrix=[list(map(int,input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        Matrix[i][j]=Matrix[i][j]%1000
#print(Matrix)

def Multiply(Matrix1,Matrix2):
    Matrix3=[[0]*(N) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                Matrix3[i][j]+=(Matrix1[i][k]*Matrix2[k][j])

            Matrix3[i][j]=Matrix3[i][j]%1000
            
            
    return Matrix3

    
    

def Expo(idx):
    if idx==1:
        return Matrix
    tmp=Expo(idx//2)
    if idx%2==1:
        return Multiply(Matrix,Multiply(tmp,tmp))
    else:
        return Multiply(tmp,tmp)
        
       
    
    
    
for i in range(N):
    print(*Expo(M)[i])
