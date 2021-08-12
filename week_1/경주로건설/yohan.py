from collections import deque
import math


def solution(board):
    # 하드코딩 방지용 매크로 변수들
    UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3
    DIRS = [UP, DOWN, LEFT, RIGHT]
    NOT_WALL, WALL = 0, 1

    def bfs(start):
        # 방향설정 index == 0(위), 1(아래), 2(왼쪽), 3(오른쪽)
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        # costs 배열을 무한대 초기화
        costs = [[math.inf for j in range(len(board[i]))]
                 for i in range(len(board))]

        # 큐 초기화 및 시작변수 대입
        queue = deque()
        queue.append(start)

        costs[0][0] = 0
        while queue:
            x, y, direction, cost = queue.popleft()
            for direction in DIRS:
                # 방향벡터 설정
                nx, ny = x + dx[direction], y + dy[direction]

                # board를 벗어났을 때 예외처리
                if nx < 0 or nx >= len(board) or ny < 0 or ny >= len(board):
                    continue
                # 벽으로 채워진 칸에 도착했을 때 예외처리
                if board[nx][ny] == WALL:
                    continue

                if board[nx][ny] == NOT_WALL:
                    # 이동중이던 방향과 같으면 직선도로, 아니면 코너로 간주하여 비용 계산
                    if direction == direction:
                        new_cost = cost + 100
                    else:
                        new_cost = cost + 600

                    # costs에 있는 값보다 계산된 비용이 적을 경우 해당 테이블의 값 업데이트하고
                    # 큐에 변수들 추가
                    if new_cost < costs[nx][ny]:
                        costs[nx][ny] = new_cost
                        queue.append((nx, ny, direction, new_cost))

        # 도착지점의 값 반환
        return costs[-1][-1]

    # 오른쪽 출발과 아래로 출발했을 때의 최소값 반환
    return min(bfs((0, 0, DOWN, 0)), bfs((0, 0, RIGHT, 0)))
