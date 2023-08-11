import sys
input=sys.stdin.readline
n = int(input())
x = []
y = []
cnt = 0

for i in range(n):
    a, b, c = map(int, input().split())
    for j in range(c):
        x.append(a)
        y.append(b)
        cnt += 1

x.sort()
y.sort()
cnt += 1 if cnt % 2 != 0 else 0

print(x[cnt // 2 - 1], y[cnt // 2 - 1])