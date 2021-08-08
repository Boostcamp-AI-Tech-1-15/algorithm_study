def solution(board):
    ## dp 반복 위한 0 개수 count 
    count0=0
    for l in board:
        count0+=l.count(0)
        
    ## dp 위한 price board선언
    board_size=len(board)
    price_board=[[[count0*600 for _ in range(4)]for _ in range(board_size)]for _ in range(board_size)]
    price_board[0][0]=[0,0,0,0] #시작 위치 초기화, 상하좌우
    
    
    ## dp 갱신, 0 개수만큼
    for _ in range(count0):
        for r in range(board_size):
            for c in range(board_size):
                if board[r][c]!=1:  #현재 위치 벽 아님
                    # 상
                    if r-1>=0 and board[r-1][c]==0: # 범위 이내, 벽이 아니라면
                        price_board[r-1][c][0]=min(price_board[r-1][c][0],price_board[r][c][0]+100,price_board[r][c][1]+600,price_board[r][c][2]+600,price_board[r][c][3]+600) #현재 값, 상하좌우와 비교 

                    # 하
                    if r+1<board_size and board[r+1][c]!=1: # 범위 이내, 벽이 아니라면
                        price_board[r+1][c][1]=min(price_board[r+1][c][1],price_board[r][c][0]+600,price_board[r][c][1]+100,price_board[r][c][2]+600,price_board[r][c][3]+600) #현재 값, 상하좌우와 비교 

                    # 좌
                    if c-1>=0 and board[r][c-1]!=1: # 범위 이내, 벽이 아니라면
                        price_board[r][c-1][2]=min(price_board[r][c-1][2],price_board[r][c][0]+600,price_board[r][c][1]+600,price_board[r][c][2]+100,price_board[r][c][3]+600) #현재 값, 상하좌우와 비교 

                    # 우
                    if c+1<board_size and board[r][c+1]!=1: # 범위 이내, 벽이 아니라면
                        price_board[r][c+1][3]=min(price_board[r][c+1][3],price_board[r][c][0]+600,price_board[r][c][1]+600,price_board[r][c][2]+600,price_board[r][c][3]+100) #현재 값, 상하좌우와 비교 

                        
    answer=min(price_board[board_size-1][board_size-1])
    return answer
