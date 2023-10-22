"""
0   0            g(0~1) 1
1   1            g(2~3) 3
10  1            G(4~7) 8
11  2            g(8~15) 20
100 1            g(2^(n)~2^(n+1)-1)=2^(n-1)*n+2^n
                                   =2^(n-1)(n+2)
101 2
110 2
111 3 
1000 1 
1001 2
1010 2
1011 3
1100 2
1101 3
1110 3
1111 4
10000 1
10001 2
10010 2
10011 3
10100 2
10101 3
10110 3

14=8+4+2
"""
import sys,math
sys.setrecursionlimit(10**8)
input=sys.stdin.readline
A,B=map(int,input().split())
def binary(num):
    return bin(num)[2:]
def sectionSum(k):
    ans=1
    for i in range(1,k):
        ans+=(2**(i-1)*(i+2))
    ans+=1
    return ans
    

def f(num):
    
    if num<=1:
        return num    
    
    k=math.log2(num)
    
    if num==2**(int(k)):
        return sectionSum(int(k))
    
    ans=0
    bi=binary(num)
    
    n=len(bi)
    cnt=0
    for i in range(n):
        if bi[i]=='1':
            ans+=f(2**(n-1-i))
            ans+=cnt*(2**(n-1-i))
            cnt+=1
    return ans

                
print(f(B)-f(A-1))        