import sys
input=sys.stdin.readline
n=int(input())
graph=[[] for i in range(n)]
for i in range(n):
  string=input()
  for j in range(n):
    graph[i].append(int(string[j]))
result=[]
def DFS(a,b,size):
  global result
  start=graph[a][b]
  
  for i in range(a,a+size):
    for j in range(b,b+size):
      if graph[i][j]!=start:
        mid=size//2
        result.append('(')
        DFS(a,b,mid)
        DFS(a,b+mid,mid)
        DFS(a+mid,b,mid)
        DFS(a+mid,b+mid,mid)
        result.append(')')
        return
  
  result.append(str(start))

DFS(0,0,n)
print(''.join(result))
  