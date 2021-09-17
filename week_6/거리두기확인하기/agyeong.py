from collections import deque

ds = ((-1, 0), (0, 1), (1, 0), (0, -1)) # 상, 우, 하, 좌

def solution(places):
    ret = []
    
    for place in places:
        q = deque()
        for i, row in enumerate(place):
            for j, col in enumerate(row):
                if place[i][j] == 'P':         
                    q.append((i, j, i, j, 0))  # 사람의 위치(i, j), 현재 위치(i, j), 거리 
        
        ret.append(0) # 일단 지키지 않는다고 가정
        
        while q:
            px, py, cx, cy, i = q.popleft()    # 사람의 위치(px, py), 현재 위치(cx, cy), 거리(i)
            for dx, dy in ds:                  # 상, 우, 하, 좌 하나씩 확인 
                nx, ny = cx + dx, cy + dy      # 현재 위치에 값을 더해서 다음 위치를 지정 
                
                if (nx == px and ny == py) or not (0 <= nx < 5 and 0 <= ny < 5) or place[nx][ny] == 'X':
                # 사람의 위치와 현재 위치가 같거나(다시 되돌아 온 경우), 대기실을 벗어났거나, 파티션이 있으면:
                    continue # 끝. 다음 위치 확인 
                    
                if place[nx][ny] == 'P': # 사람이 있으면!? 거리두기 지키지 않은 것
                    break # break 걸어서 for문 멈춘다. 
                
                if not i: # 거리가 0이면 한칸 더 확인. 
                    q.append((px, py, nx, ny, 1))
                    
            else: # for문이 break로 끝난 게 아닐때 실행됨. (break를 만나지 않았을 때 실행됨)
                continue
                
            break # break로 끝났으면 continue가 실행되지 않기 때문에 35 line의 break를 만나고, 이는 while를 멈추게한다. 
            
        else: # break를 만나지 않았을 때 실행됨. 즉, 거리두기를 지키지 않은 사람이 없다. 
            ret[-1] = 1 # 거리두기 지키고 있음. 
            
    return ret