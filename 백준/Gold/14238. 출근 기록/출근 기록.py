import sys
input=sys.stdin.readline
from collections import defaultdict
dic=defaultdict(int)
dic1=defaultdict(int)

dp=[[[[0]*(26) for _ in range(50)] for _ in range(50)] for _ in range(50)]

s=input().rstrip('\n')

arr=['','A','B','C','AA','AB','AC','BA','BC','CA','CB','AAA','AAB','AAC','ABA','ABC','ACA','ACB','BAA','BAB','BAC','BCA','BCB','CAA','CAB','CBA']

for i in range(26):
    dic1[arr[i]]=i

for si in s:
    dic[si]+=1

ans=[]
def DFS(a,b,c,res):
    #print(a,b,c,res)
    if a>dic['A'] or b>dic['B'] or c>dic['C']:
        return

    if a+b+c>len(s):
        return
    if len(ans)>0:
        return

    if a+b+c>0 and a==dic['A'] and b==dic['B'] and c==dic['C']:
        ans.append(res)
        return

    if len(res)<2:
        if dp[a][b][c][dic1[res]]:
            return
        dp[a][b][c][dic1[res]]=1
        if len(res)==0:
            DFS(a+1,b,c,res+'A')
            DFS(a,b+1,c,res+'B')
            DFS(a,b,c+1,res+'C')

        elif len(res)==1:
            if res[-1]=='A':
                DFS(a+1,b,c,res+'A')
                DFS(a,b+1,c,res+'B')
                DFS(a,b,c+1,res+'C')

            elif res[-1]=='B':
                DFS(a+1,b,c,res+'A')
                DFS(a,b,c+1,res+'C')

            elif res[-1]=='C':
                DFS(a+1,b,c,res+'A')
                DFS(a,b+1,c,res+'B')
                
    else:
        if len(res)==2:
            if dp[a][b][c][dic1[res]]:
                return
            dp[a][b][c][dic1[res]]=1
        else:
            if dp[a][b][c][dic1[res[-3:]]]:
                return 
            dp[a][b][c][dic1[res[-3:]]]=1

        if (res[-2]=='A' and res[-1]=='A') or (res[-2]=='B' and res[-1]=='A'):
            DFS(a+1,b,c,res+'A')
            DFS(a,b+1,c,res+'B')
            DFS(a,b,c+1,res+'C')

        elif (res[-2]=='A' and res[-1]=='B'):
            DFS(a+1,b,c,res+'A')
            DFS(a,b,c+1,res+'C')
            
        elif(res[-2]=='A' and res[-1]=='C') or (res[-2]=='B' and res[-1]=='C') or (res[-2]=='C' and res[-1]=='A'):
            DFS(a+1,b,c,res+'A')
            DFS(a,b+1,c,res+'B')

        elif (res[-2]=='C' and res[-1]=='B'):
            DFS(a+1,b,c,res+'A')
            



DFS(0,0,0,'')
print(ans[0] if len(ans)>0 else -1)
    