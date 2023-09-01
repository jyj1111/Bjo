import sys
input=sys.stdin.readline

n=int(input())## n은 3~8
arr=list(map(int,input().split()))

checked=[0]*(n)
maxDis=0
def Distance(arr1):
    global maxDis    
    if len(arr1)==n:
        dis=0
        for j in range(n-1):
            dis+=abs(arr1[j+1]-arr1[j])
        maxDis=max(maxDis,dis)
    else:
        for i in range(n):
            if not checked[i]:
                checked[i]=1
                arr1.append(arr[i])
                Distance(arr1)
                checked[i]=0
                arr1.pop()
               
Distance([])
print(maxDis)