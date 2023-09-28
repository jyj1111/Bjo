import sys
input=sys.stdin.readline
n=int(input()) #1 ≤ n ≤ 80

answer=['1']

def nearCheck(arr,s1):
    s=''.join(arr)+s1
    mid=len(s)//2
    for k in range(1,mid+1):
        if s[-2*k:-k]==s[-k:]:
            return False
    #print(s)
    return True
    
    

def DFS(depth):
    global answer
    #print(answer)
    if depth==n:
        print(''.join(answer))
        sys.exit(0)

    else:
        for i in range(1,4):
            if nearCheck(answer,str(i)):
                answer.append(str(i))
                DFS(depth+1)
                answer.pop()

DFS(1)