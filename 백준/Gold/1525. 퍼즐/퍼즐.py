import sys
input=sys.stdin.readline
from collections import defaultdict,deque

dic=defaultdict(int)

start=""
for i in range(3):
    start+=input().rstrip('\n').replace(" ","")

def BFS(s):
    queue=deque()
    queue.append(s)
    while queue:
        s1=queue.popleft()
        if s1=='123456780':
            return dic[s1]
            
        pos=s1.find('0')
        y,x=pos//3,pos%3
        for dy,dx in [(-1,0),(0,1),(1,0),(0,-1)]:
            y1=y+dy
            x1=x+dx
            if 0<=y1<3 and 0<=x1<3:
                pos1=3*y1+x1
                s2=list(s1)
                s2[pos1],s2[pos]=s2[pos],s2[pos1]
                s2=''.join(s2)
                if not dic[s2]:
                    dic[s2]=dic[s1]+1
                    queue.append(s2)


    return -1

print(BFS(start))