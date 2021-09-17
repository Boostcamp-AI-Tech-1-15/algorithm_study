from collections import deque

def solution(places):
    ans = []
    d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for place in places:
        p_list = []
        for i in range(5):
            for j in range(5):
                if place[i][j]=='P':
                    p_list.append((i, j))
        is_ok = True
        for p in p_list:
            q = deque([(*p, 0)])
            visit = set()
            while q:
                x, y, cnt  = q.popleft()
                
                if (x, y)!=p and place[x][y]=='P':
                    if cnt<=2:
                        ans.append(0)
                        is_ok = False
                    break
                    
                for i, j in d:
                    next_x = x + i
                    next_y = y + j
                    if 0<=next_x<5 and 0<=next_y<5 \
                    and (next_x, next_y) not in visit \
                    and place[next_x][next_y]!='X':
                        q.append((next_x, next_y, cnt+1))
                        visit.add((next_x, next_y))
                        
            if is_ok==False:
                break
            
        if is_ok==True:
            ans.append(1)
    return ans