import sys
input=sys.stdin.readline
exp=input().rstrip("\n")
exp1=exp.split('-')
answer=0
if exp[0]=='-':
  exp1=exp1[1:]
else:
  exp2=exp1[0].split('+')
  answer+=2*sum(list(map(int,exp2)))
for item in exp1:
  exp2=item.split('+')
  answer-=sum(list(map(int,exp2)))

print(answer)