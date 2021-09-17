from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
    
def check(r1, c1, r2, c2):
    if abs(r1 - r2) + abs(c1 - c2) > 2:
        return False
    return True
    
def bfs(place, sr, sc):
    q = deque([(sr, sc)])
    visited = [[False]*5 for _ in range(5)]
    while q:
        r, c = q.popleft()
        visited[r][c] = True
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if not check(sr, sc, nr, nc):
                continue
            if not 0 <= nr < 5 or not 0 <= nc < 5:
                continue
            if not visited[nr][nc]:
                if place[nr][nc] == 'P':
                    return 0 
                if place[nr][nc] == 'O':
                    q.append((nr, nc))
    return 1


def solution(places):
    answer = []

    for p in places:
        p_pos = []
        for i in range(5):
            for j in range(5):
                if p[i][j] == 'P':
                    p_pos.append((i, j))

        for r, c in p_pos:
            if not bfs(p, r, c):
                answer.append(0)
                break
        else:
            answer.append(1)
            
    return answer