import sys
from collections import defaultdict
input=sys.stdin.readline
T=int(input())

def Find(x):
    if parents[x]!=x:
        parents[x]=Find(parents[x])
    return parents[x]

def Union(i,j):
    i=Find(i)
    j=Find(j)
    if i<j:
        parents[j]=i
        relation[i]+=relation[j]
    elif i>j:
        parents[i]=j
        relation[j]+=relation[i]
    else:
        return
        
      

for i in range(T):
    F=int(input())# F<=100000
    dic=defaultdict(int)
    relation=defaultdict(int)
    parents=[0]
    for j in range(F):
        p1,p2=input().split()
        l=len(dic)
        #print(dic)
        #print(relation)
        #print(parents)
        if p1 not in dic and p2 not in dic:
            parents.append(l+1)
            parents.append(l+2)
            dic[p1]=l+1
            dic[p2]=l+2
            
            relation[l+1]+=1
            relation[l+2]+=1
            print(2)
            Union(l+1,l+2)
            
           
        elif p1 in dic and p2 not in dic:
            parents.append(l+1)
            dic[p2]=l+1
            relation[l+1]+=1
            print(relation[Find(dic[p1])]+relation[l+1])
            Union(dic[p1],l+1)
                       
            
        elif p1 not in dic and p2 in dic:
            parents.append(l+1)
            dic[p1]=l+1
            relation[l+1]+=1
            print(relation[Find(dic[p2])]+relation[l+1])
            Union(dic[p2],l+1)
            
            
            
        else:
            if Find(dic[p1])==Find(dic[p2]):
                print(relation[Find(dic[p1])])
            else:
                print(relation[Find(dic[p1])]+relation[Find(dic[p2])])
            #print(dic[p1],dic[p2])
            Union(dic[p1],dic[p2])