import sys
input=sys.stdin.readline
n=int(input())
hw=[]
maxDay=0
for i in range(n):
    day,w=map(int,input().split())
    maxDay=max(maxDay,day)
    hw.append((day,w))

hw.sort(key=lambda x:-x[1])

point=[0]*(maxDay+1)

answer=0

for day,w in hw:
    for d in range(day,0,-1):
        if point[d]:
            continue
        else:
            point[d]=w
            answer+=w
            break
    
print(answer)    