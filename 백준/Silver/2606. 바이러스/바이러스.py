import sys
n=int(sys.stdin.readline())
graph=[ [0]* n   for _ in range(n)]
for i in range(int(sys.stdin.readline())):
    a,b=map(int,input().split());
    graph[a-1][b-1]=1;
    graph[b-1][a-1]=1;
count=0;
start=0;
arr=[];
arr.append(start);
while arr:
    visit=arr.pop();
    
    for j in range(0, n):
        if graph[visit][j]==1:
            
            graph[visit][j]=2
            graph[j][visit]=2
            if j not in arr:
                arr.append(j)
                count+=1;

print(count);              