from collections import deque

# 현재 + 과거 인덱스 더한 값이 같게 하기 위해
# 하 + 상 == 좌 + 우 == 3
# 하 좌 우 상
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]


def solution(board):
    n = len(board)
    check = [[0] * n for _ in range(n)]

    def bfs(x, y, cost, direction):
        q = deque([(x, y, cost, direction)])
        while q:
            x, y, cost, direction = q.popleft()
            # 하 좌 우 상
            for i in range(4):
                nx, ny, nc = x + dx[i], y + dy[i], cost + 100
                # 직선도로 반대방향으로 돌아가면 pass
                if i + direction == 3:
                    continue
                # 이외로 방향 바뀌면 코너
                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    continue
                if direction != i and direction != -1:
                    nc += 500
                if not board[nx][ny]:
                    if not check[nx][ny] or check[nx][ny] >= nc:
                        check[nx][ny] = nc
                        q.append([nx, ny, nc, i])

    bfs(0, 0, 0, -1)
    # print(check)
    return check[n - 1][n - 1]
