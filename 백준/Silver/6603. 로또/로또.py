import sys
input=sys.stdin.readline


def DFS(idx,num,ans):
    global arr
    #print(idx,ans)
    if len(ans)==6:
        print(*ans)
        return
    
    for i in range(idx,num):
        if idx==0:
            DFS(idx+1,num,ans+[arr[i]])
        else:
            if arr[i] not in ans and arr[i]>ans[idx-1]:
                DFS(idx+1,num,ans+[arr[i]])
        

        
        

while True:
    inputList=list(map(int,input().split()))
    num=inputList[0]
    if num==0:
        break
    arr=inputList[1:]
    DFS(0,num,[])
    print()