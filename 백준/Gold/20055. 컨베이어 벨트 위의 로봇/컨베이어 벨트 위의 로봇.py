"""
1.1은 올리는 위치, N은 내리는 위치
2.올리거나 움직이면 그 칸의 내구도는 1이 감소
3. 올리는 위치의 내구도가 0이면 더 이상 올릴 수가 없다.
3. 이동하기 위해서는 내구도가 1이상이거나 그 칸에 로봇이 없어야 한다.
4. 내구도가 0인 칸이 K개 이상이면 종료

"""
import sys
from collections import deque
input=sys.stdin.readline
N,K=map(int,input().split()) #2 ≤ N ≤ 100 , 1<=K<=2N
belt=list(map(int,input().split()))
robots=[0]*(N)              

def check():
    global belt
    if belt.count(0)>=K:
        return True
    return False

def move_belt():
    global belt,robots
    belt=[belt[-1]]+belt[:-1] #벨트 1칸 이동
    robots=[0]+robots[:-1]    #로봇 1칸 이동
    robots[-1]=0              # 로봇이 내리는 위치에 있을시 즉시 내림
        
    
def move_robot():
    global belt,robots
    for i in range(N-2,0,-1): # 내구도가 0보다 크고 옆에 로봇이 없으면 이동
        if robots[i]==1 and robots[i+1]==0 and belt[i+1]>0:
            robots[i],robots[i+1]=0,1
            belt[i+1]-=1  # 내구도 1 감소
    
def push_robot():
    global belt,robots
    if belt[0]>0: # 올리는 위치의 내구도가 0보다 크면 올림
        robots[0]=1
        belt[0]-=1 # 내구도 1 감소

ans=0
while True:
    ans+=1
    move_belt()
    move_robot()
    push_robot()
    if check():
        break
    

print(ans)