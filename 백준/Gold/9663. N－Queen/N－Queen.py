import sys
input=sys.stdin.readline

n=int(input())

ans=0

row=[0]*(n)

def check(now):
    for j in range(now):
        if row[j]==row[now] or abs(row[j]-row[now])==now-j:
            return False
    return True
        

    
def Queen(now):
    global ans
    if now==n:
        ans+=1

    else:
        for i in range(n):
            row[now]=i
            if check(now):
                Queen(now+1)      



Queen(0)
print(ans)