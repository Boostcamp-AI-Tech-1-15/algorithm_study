from collections import deque

def solution(board):
    n = len(board)
    ans = 0
    d = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    q = deque([((0, 0), (0, 1), 0)])
    visit = set()
    
    while q:
        head, tail, t = q.popleft()
        if (head, tail) in visit or (tail, head) in visit:
            continue
            
        visit.add((head, tail))
        visit.add((tail, head))
        
        if head==(n-1, n-1) or tail==(n-1, n-1):
            break
            
        hx, hy = head
        tx, ty = tail
        
        for i, j in d:
            next_hx, next_hy = hx+i, hy+j
            next_tx, next_ty = tx+i, ty+j
            
            if 0<=next_hx<n and 0<=next_hy<n \
            and 0<=next_tx<n and 0<=next_ty<n \
            and board[next_hx][next_hy]==0 \
            and board[next_tx][next_ty]==0:
                q.append(((next_hx, next_hy), (next_tx, next_ty), t+1))

        if hx==tx:
            if hx+1<n and board[hx+1][hy]==0 and board[tx+1][ty]==0: # - 모양, 아래
                q.append(((hx, hy), (hx+1, hy), t+1))
                q.append(((tx, ty), (tx+1, ty), t+1))

            if hx-1>=0 and board[hx-1][hy]==0 and board[tx-1][ty]==0: # - 모양, 위
                q.append(((hx, hy), (hx-1, hy), t+1))
                q.append(((tx, ty), (tx-1, ty), t+1))
        elif hy==ty:
            if hy+1<n and board[hx][hy+1]==0 and board[tx][ty+1]==0: # l 모양, 오른쪽
                q.append(((hx, hy), (hx, hy+1), t+1))
                q.append(((tx, ty), (tx, ty+1), t+1))
            if hy-1>=0 and board[hx][hy-1]==0 and board[tx][ty-1]==0: # l 모양, 왼쪽
                q.append(((hx, hy), (hx, hy-1), t+1))
                q.append(((tx, ty), (tx, ty-1), t+1))
    
    ans = t
    return ans