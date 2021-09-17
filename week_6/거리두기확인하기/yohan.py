from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(place, x, y):
    q = deque()
    visited = [[False] * 5 for _ in range(len(place))]
    
    q.append((x, y, 0))
    visited[x][y] = True
    
    while q:
        x, y, depth = q.popleft()
        if depth == 2:
            continue
            
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < 5 and 0 <= ny < 5:
                if visited[nx][ny]:
                    continue
                if place[nx][ny] == 'P':
                    return False
                if place[nx][ny] == 'O':
                    q.append((nx, ny, depth + 1))
                    visited[nx][ny] = True
    
    return True

def solution(places):
    answer = []
    
    for place in places:
        p = [list(place[i]) for i in range(len(place))]
        flag = True
        for i in range(len(p)):
            for j in range(len(p)):
                if p[i][j] == 'P':
                    if not bfs(place, i, j):
                        flag = False
            if not flag:
                break
                
        if flag:
            answer.append(1)
        else:
            answer.append(0)
    
    return answer
