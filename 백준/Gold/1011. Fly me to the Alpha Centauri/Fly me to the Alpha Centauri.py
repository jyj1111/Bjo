import sys
input=sys.stdin.readline

t=int(input())

#  1  2   2  1
#        1  
for i in range(t):
    
    x,y=map(int,input().split())
    y=y-x
    cnt=1
    if y==1:
        print(cnt)
    else:
        while True:
            hap=0
            mid=cnt//2
            if cnt%2==1:
                hap=(mid+1)**2
            else:
                hap=mid*(mid+1)
                
            if cnt<=y<=hap:
                break
            cnt+=1
        print(cnt)