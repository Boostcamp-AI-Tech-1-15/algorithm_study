from collections import deque

ds = ((0, 1), (1, 0), (0, -1), (-1, 0)) # 상 우 하 좌 (시계방향)

def solution(board):
    n, m = len(board), len(board[0]) # 가로 세로 길이 
    result = [[0] * m for _ in range(n)] # 최소 비용 저장할 빈 리스트 
    
    q = deque([[0, 0, 0, 0], [0, 0, 1, 0]]) # row, col, direction index, cost / 출발할 때 방향 2개 (오른쪽, 아래쪽)
    while q:
        cur_x, cur_y, last_d, cost = q.popleft()
        for dd in [-1, 0, 1]: # 왔던 길 반대방향 제외하고 모두 다 방문 
            cur_d = (last_d + dd) % 4 # 현재 가야하는 방향
            nx, ny = cur_x + ds[cur_d][0], cur_y + ds[cur_d][1] # 다음 위치 row, col 
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0: #
                if cur_d == last_d and (result[nx][ny] == 0 or result[nx][ny] >= cost+100): 
                # 직진이고 현재 위치에서 다음 위치로 가는 비용이 (기존 비용보다) 더 작다면 
                    result[nx][ny] = cost + 100 # 비용 업데이트 
                    q.append((nx, ny, cur_d, cost + 100)) # q 추가 (다음에 방문하기 위해서)
                elif cur_d != last_d and (result[nx][ny] == 0 or result[nx][ny] >= cost+600):
                # 코너이고 현재 위치에서 다음 위치로 가는 비용이 (기존 비용보다) 더 작다면
                    result[nx][ny] = cost + 600 # 비용 업데이트 
                    q.append((nx, ny, cur_d, cost + 600)) # q 추가 (다음에 방문하기 위해서)
                    
    return result[-1][-1]