import sys
from collections import deque
import heapq
input = sys.stdin.readline

maxdic = {}
mindic = {}
num = int(input())
maxheap = []
minheap = []
visit = [False]*100001
for i in range(num):
    problemNumber , difficulty = map(int,input().split(" "))
    heapq.heappush(maxheap,((-1*difficulty),-1*problemNumber))
    heapq.heappush(minheap,(difficulty,problemNumber))
    visit[problemNumber] = True
    maxdic[-1*problemNumber] = (-1*difficulty)
    mindic[problemNumber] = difficulty
num = int(input())

for i in range(num):
    command = input().split(" ")
    if command[0] == "add" :
        heapq.heappush(maxheap,((-1*int(command[2])),-1*int(command[1])))
        heapq.heappush(minheap,(int(command[2]),int(command[1])))
        visit[int(command[1])] = True
        maxdic[-1*int(command[1])] = -1*int(command[2])
        mindic[int(command[1])] = int(command[2])
    elif command[0] == "recommend" and int(command[1]) == 1:
        while True :
            if visit[-1*maxheap[0][1]] == False :
                heapq.heappop(maxheap)
            elif maxdic[maxheap[0][1]] != maxheap[0][0] :
                heapq.heappop(maxheap)
            else : 
                break
        # target = heapq.heappop(maxheap)
        print(-1*maxheap[0][1])
        # visit[-1*maxheap[0][1]] = False
    elif command[0] == "recommend" and int(command[1]) == -1:
        while True :
            if visit[minheap[0][1]] == False :
                heapq.heappop(minheap)
            elif mindic[minheap[0][1]] != minheap[0][0] :
                heapq.heappop(minheap)
            else : 
                break
        # target = heapq.heappop(minheap)
        print(minheap[0][1])
        # visit[minheap[0][1]] = False
    else :
        visit[int(command[1])] = False
