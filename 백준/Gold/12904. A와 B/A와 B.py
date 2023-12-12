import sys
input=sys.stdin.readline
        
S=input().rstrip('\n')
T=input().rstrip('\n')


while len(T)>=len(S) and T!=S:
    
    if T[-1]=='A':
        T=T[:-1]
    else:
        T=T[:-1][::-1]

if T==S:
    print(1)
else:
    print(0)