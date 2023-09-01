import sys
input=sys.stdin.readline

from itertools import combinations

L,C=map(int,input().split())## L,C은 3~15
arr=list(map(str,input().split()))

g1=[]##모음
g2=[]##자음

for ch in arr:
    if ch in ['a', 'e', 'i', 'o', 'u']:
        g1.append(ch)
    else:
        g2.append(ch)

ansArr=[]
for num1 in range(1,len(g1)+1):## 모음의 개수 범위
    for num2 in range(2,len(g2)+1):## 자음의 개수 범위
        if num1+num2==L:
            for mo in list(combinations(g1,num1)): ## 모음의 조합
                for ja in list(combinations(g2,num2)):## 자음의 조합
                    arr1=list(mo)+list(ja) ## 리스트화
                    arr1.sort() ## 알파벳순 정렬
                    s1=''.join(arr1) ## 문자열화 
                    ansArr.append(s1)
ansArr.sort() ## 정답 문자열배열 정렬
for ans in ansArr:
    print(ans)
