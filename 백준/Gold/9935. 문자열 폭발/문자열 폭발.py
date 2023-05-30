import sys

input=sys.stdin.readline
string=input().strip('\n')
bomb=input().strip('\n')
answer=[]
for ch in string:
  answer.append(ch)
  if len(answer)>=len(bomb) and ''.join(answer[-len(bomb):])==bomb:
    del answer[-len(bomb):]
  
  
if answer:
  print(''.join(answer))
else:
  print('FRULA')