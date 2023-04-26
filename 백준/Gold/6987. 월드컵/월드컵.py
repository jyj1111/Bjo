import sys
from itertools import combinations
input=sys.stdin.readline
cases=list(combinations(range(6),2))
           
def DFS(depth,arr):
  global cnt
  
  if depth==15:
    cnt=1
    
    for subarr in arr:
      if subarr.count(0)!=3:
        cnt=0    
        break
    
    return        
                
  home,away=cases[depth]
  for x,y in ((0,2),(1,1),(2,0)):
     if arr[home][x]>0 and arr[away][y]>0:
       arr[home][x]-=1
       arr[away][y]-=1
       DFS(depth+1,arr)
       arr[home][x]+=1
       arr[away][y]+=1    
        
for i in range(4):
    arr=list(map(int,input().split()))
    arr1=[]
    for j in range(0,16,3):
        arr1.append(arr[j:j+3])
    cnt=0
    DFS(0,arr1)
    print(cnt,end=' ')