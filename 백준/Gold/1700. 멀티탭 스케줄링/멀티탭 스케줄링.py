import sys
input=sys.stdin.readline
n,k=map(int,input().split())
arr=list(map(int,input().split()))
plugs=[]
cnt=0
for i in range(k):
    if plugs.count(arr[i])>0:
        continue
    if len(plugs)<n:
        plugs.append(arr[i])
        continue
    
    max_idx=0
    sel_idx=0
    for j in range(len(plugs)):
        try:
            idx=arr[i:].index(plugs[j])
        except:
            idx=k
        finally:
            if max_idx<idx:
                max_idx=idx
                sel_idx=j
    plugs[sel_idx]=arr[i]
    cnt+=1
         
print(cnt)            