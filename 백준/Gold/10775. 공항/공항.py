import sys
sys.setrecursionlimit(10**8)
input=sys.stdin.readline

"""
가능한 큰 게이트에 비행기를 도킹시킨다. ->그리디
비행기를 게이트에 도킹후 (게이트번호-1)번 게이트하고 연결이 된다.-> 유니온 파인드
비행기를 게이트에 도킹시킬때 find 연산후 0이면 종료한다.
시간 복잡도: plog(g)
"""



def find(x):
    if parents[x]!=x:
        parents[x]=find(parents[x])
    return parents[x]

def union(x,y):
    x=find(x)
    y=find(y)
    if x<y:
        parents[y]=x
    elif x>y:
        parents[x]=y
    else:
        return
    
def init():
    for i in range(gateNum+1):
        parents[i]=i

        
gateNum=int(input())
planeNum=int(input())

parents=[0]*(gateNum+1)
init()
ans=0
stop=False # 비행기가 중간에 도킹을 멈추는 플래그
for i in range(planeNum):
    gate=int(input())
    gate=find(gate)
    if gate==0:
        ans=i
        stop=True
        break
    else:
        union(gate,gate-1)

if stop:
    print(ans)
else:
    print(planeNum)
