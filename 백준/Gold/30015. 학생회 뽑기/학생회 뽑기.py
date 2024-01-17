import sys

input=sys.stdin.readline
n, k = map(int, input().split())  # 1<=n<=200000, 1<=k<=n
arr = list(map(int, input().split()))

# 최종 결과를 저장할 변수를 초기화합니다.
ans = 0

# 각 비트에 대해
for i in range(19, -1, -1):
    # 현재 비트가 1인 숫자들만 선택합니다.
    tmp = [num for num in arr if num & (1 << i)]

    # 선택된 숫자가 k개 이상이면, 해당 비트를 결과에 추가합니다.
    if len(tmp) >= k:
        ans |= (1 << i)
        arr = tmp

print(ans)