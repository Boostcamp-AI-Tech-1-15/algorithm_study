from collections import deque
import sys
def solution(board):
    answer = 0

    dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    # 아래, 오른쪽, 위, 왼쪽
    cost_map = [[sys.maxsize] * len(board[0]) for _ in range(len(board))]

    x, y = 0, 0
    cost_map[y][x] = 0
    q = deque([]) # bfs에서 사용할 q

    for i in range(2):
        dx, dy = dirs[i][0], dirs[i][1]
        nx, ny = x + dx, y + dy
        cost = 100
        if board[ny][nx] != 1:
            q.append([nx, ny, cost, i])
            cost_map[ny][nx] = 100
        '''
        처음 시작점에서 오른쪽, 아래로 시작하는 방향으로 경주로를 건설
        해당 두 위치를 cost_map을 100원으로 설정
        단 시작 두 위치중 건설 할 수 없는 곳이 있으면 하지 않는다.
        '''

    while q:
        x, y, before_cost, before_dir = q.popleft()
        # q에 저장되었던 이전경로에 대한 값들


        for i, d in enumerate(dirs):
            nx = x + d[0]
            ny = y + d[1]
            cur_dir = i
            # 방향과 새 좌표 설정

            if 0 <= nx < len(board[0]) and 0 <= ny < len(board) and board[ny][nx] != 1:
                # 맵의 밖으로 나가지 않고 1이 아니면

                cost = 100 if cur_dir == before_dir else 600
                cur_cost = before_cost + cost
                # 이전 방향과 같으면 100원 아니면 600
                # 되돌아 가는 것도 엄밀히 말하면 100원의 직진이지만 어차피 그럴 경우는 cost가 높아질수 밖에 없다.

                if cur_cost <= cost_map[ny][nx]:
                    # 저장되었던 코스트보다 적으면 다음 q에 넣어 확인하다
                    # 같은 코스트라도 이전 경로에따라 다음 값이 달라지기 때문에 < 가 아니라 <=로 설정
                    cost_map[ny][nx] = cur_cost
                    # 작거나 같은경우 코스트값 갱신
                    q.append([nx, ny, cur_cost, i])
                    # 다음 q에 append


    return cost_map[-1][-1]


solution([[0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 0, 1, 0, 0], [1, 0, 0, 0, 1], [0, 1, 1, 0, 0]])