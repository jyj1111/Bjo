from collections import deque

INF = 10001
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def is_valid(x, y, n, m):
    return 0 <= x < n and 0 <= y < m

def solution(storage, requests):
    n, m = len(storage), len(storage[0])
    grid = [[ord(cell) - ord('A') for cell in row] for row in storage]

    for request in requests:
        target = ord(request[0]) - ord('A')

        if len(request) == 2:
            grid = [[-1 if cell == target else cell for cell in row] for row in grid]
            continue

        memo = [[INF] * m for _ in range(n)]
        targets_to_remove = []
        queue = deque()

        for i in range(n):
            for j in range(m):
                if (i in {0, n - 1} or j in {0, m - 1}) and memo[i][j] == INF:
                    memo[i][j] = 0 if grid[i][j] == -1 else 1
                    if grid[i][j] == target:
                        targets_to_remove.append((i, j))
                    if grid[i][j] == -1:
                        queue.append((i, j))

        while queue:
            x, y = queue.popleft()
            for dx, dy in DIRECTIONS:
                nx, ny = x + dx, y + dy
                if is_valid(nx, ny, n, m) and memo[nx][ny] == INF:
                    memo[nx][ny] = 0 if grid[nx][ny] == -1 else 1
                    if grid[nx][ny] == -1:
                        queue.append((nx, ny))
                    elif grid[nx][ny] == target:
                        targets_to_remove.append((nx, ny))

        for x, y in targets_to_remove:
            grid[x][y] = -1

    return sum(cell != -1 for row in grid for cell in row)