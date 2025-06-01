import sys
input = sys.stdin.readline
from collections import deque, defaultdict

N = int(input())  
M = int(input())  

in_degree = [0] * N 
need_graph = [defaultdict(int) for _ in range(N)]  # y → x 로 x를 만들기 위해 y가 얼마나 필요한지 저장
part_count = [defaultdict(int) for _ in range(N)]  # 기본 부품 개수 기록
queue = deque()


for _ in range(M):
    x, y, k = map(int, input().split())
    in_degree[x - 1] += 1
    need_graph[y - 1][x - 1] += k  # y → x

for i in range(N):
    if in_degree[i] == 0:
        queue.append(i)
        part_count[i][i] = 1  # 자기 자신이 기본 부품

# 위상 정렬 + 기본 부품 누적 계산
while queue:
    cur = queue.popleft()
    for nxt, cnt in need_graph[cur].items():
        for basic, num in part_count[cur].items():
            part_count[nxt][basic] += num * cnt
        in_degree[nxt] -= 1
        if in_degree[nxt] == 0:
            queue.append(nxt)

for part in sorted(part_count[N - 1].items()):
    print(part[0] + 1, part[1])