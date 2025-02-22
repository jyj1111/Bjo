from collections import deque

INF = 10001
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def is_valid(nx, ny, n, m):
    return 0 <= nx < n and 0 <= ny < m

def solution(storage, requests):
    n = len(storage)  # 행
    m = len(storage[0])  # 열
    answer = 0

    # 맵 초기화
    grid = [[ord(cell) - ord('A') for cell in row] for row in storage]

    for request in requests:
        target = ord(request[0]) - ord('A')

        # 크레인 로직 (모든 타겟 제거)
        if len(request) == 2:
            for i in range(n):
                for j in range(m):
                    if grid[i][j] == target:
                        grid[i][j] = -1
            continue

        # 지게차 로직 (연결된 타겟 제거)
        memo = [[INF] * m for _ in range(n)]
        targets_to_remove = []
        queue = deque()

        for i in range(n):
            for j in range(m):
                if i != 0 and j != 0 and i != n - 1 and j != m - 1:
                    continue
                if memo[i][j] != INF:
                    continue
                if grid[i][j] != -1:
                    memo[i][j] = 1
                    if grid[i][j] == target:
                        targets_to_remove.append((i, j))
                    continue

                memo[i][j] = 0
                queue.append((i, j))

                while queue:
                    x, y = queue.popleft()
                    for dx, dy in DIRECTIONS:
                        nx, ny = x + dx, y + dy
                        if not is_valid(nx, ny, n, m) or memo[nx][ny] != INF:
                            continue
                        if grid[nx][ny] == -1:
                            memo[nx][ny] = 0
                            queue.append((nx, ny))
                        else:
                            memo[nx][ny] = 1
                            if grid[nx][ny] == target:
                                targets_to_remove.append((nx, ny))

        # 제거 대상 처리
        for x, y in targets_to_remove:
            grid[x][y] = -1

    # 남은 컨테이너 개수 세기
    for i in range(n):
        for j in range(m):
            if grid[i][j] != -1:
                answer += 1

    return answer